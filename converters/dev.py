import sys
import glob
import yaml
import frontmatter
import rich_click as click

from .utils import API
from .utils import YAMLHandler, str_presenter


def convert_to_dev(settings, track_path, identifier):
    # Extract Settings
    config = settings['config']
    log = settings['log']

    # Validate we can open track.yml in the provided path
    try:
        with click.open_file(f'{track_path}/track.yml', mode='r') as tf_r:
            track = yaml.safe_load(tf_r)
    except FileNotFoundError as track_exception:
        log.error('Unable to load track.yml: %s', track_exception)
        sys.exit(1)

    # Validate track.yml is in the proper state to convert
    if f'-{identifier}' in track['slug']:
        log.error(
            f'It looks like the track slug '
            f'already has the {identifier} suffix.'
        )
        sys.exit(1)

    # Add identifier to track slug
    track['slug'] = track['slug'] + f'-{identifier}'

    # Add identifier to track title
    track['title'] = f'{identifier.upper()} - ' + track['title']

    # Remove IDs from assignments.md files
    assignment_paths = glob.glob(
        f'{track_path}/**/assignment.md',
        recursive=True
        )

    # Instantiate API
    api = API(config)

    track_results = api.graphql_query(query_type="track", slug=track['slug'])

    if track_results['track'] is not None:
        log.warn(
            'Track with identifier: [%s] and ID: %s already exists.',
            identifier,
            track_results['track']['id']
        )
        track_exists = True
    else:
        log.error('Track with identifier: %s does not exist', identifier)
        track_exists = False

    # Loop Through Assignments and update or remove id:
    for assignment in assignment_paths:
        try:
            with click.open_file(assignment, mode='r') as af_r:
                doc = frontmatter.loads(af_r.read())
                # Check to see if dev track already exists
                if track_exists:
                    challenge_found = [
                        challenge for challenge in
                        track_results['track']['challenges']
                        if challenge['slug'] == doc.metadata['slug']
                        ]

                    if challenge_found != []:
                        log.warn(
                            'Found Existing Assignment [%s] with ID: %s',
                            challenge_found[0]['slug'],
                            challenge_found[0]['id']
                        )
                        doc.metadata['id'] = challenge_found[0]['id']
                    else:
                        log.warn(
                            'Assignment [%s] does not exist.',
                            doc.metadata['slug']
                        )
                        doc.metadata.pop('id', None)
                else:
                    # Track not found - remove id
                    log.info(
                        'Assignment [%s] does not exist  Removing id.',
                        doc.metadata['slug']
                    )
                    doc.metadata.pop('id', None)

                assignment_output = frontmatter.dumps(
                        doc,
                        sort_keys=False,
                        handler=YAMLHandler()
                    )
                with click.open_file(assignment, mode='w') as af_w:
                    af_w.write(assignment_output)
                    # Add single newline to end of file
                    af_w.write('\n')
                    log.info(
                        'Completed update of [%s]',
                        assignment
                    )
                    af_w.close()
                af_r.close()

        except FileNotFoundError as assignment_exception:
            log.error(
                'Unable to open %s: %s',
                assignment,
                assignment_exception
            )
            sys.exit(1)

    # Remove ID from track.yml
    if track_exists:
        # Set the id in track.yml to match existing track
        log.info(
            'Setting id in track.yml to: %s',
            track_results['track']['id']
            )
        track['id'] = track_results['track']['id']
    else:
        # Track not Found, remove the id
        log.info(
            'Track [%s] not found.  Removing id.',
            track['slug']
        )
        track.pop('id', None)

    # Add representer to format multiline strings properly
    yaml.add_representer(str, str_presenter)
    # Dump track.yml
    try:
        with click.open_file(f'{track_path}/track.yml', mode='w') as tf_w:
            # Write file changes
            yaml.dump(track, tf_w, default_style=None, sort_keys=False)
            log.info('Completed update of %s/track.yml', track_path)
            log.info(
                'Track conversion to [dev] with identifier [%s] complete!',
                identifier
            )
    except PermissionError as update_exception:
        log.error('Unable to write track.yml: %s', update_exception)
        sys.exit(1)
