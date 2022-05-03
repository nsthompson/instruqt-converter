import glob
import yaml
import frontmatter
import rich_click as click


def convert_to_prod(track_path, identifier):
    # Validate we can open track.yml in the provided path
    try:
        with click.open_file(f'{track_path}/track.yml', mode='r') as tf_r:
            track = yaml.safe_load(tf_r)
    except FileNotFoundError as track_exception:
        print(f'Unable to load track.yml: {track_exception}')
        exit(1)

    # Validate track.yml is in proper state to convert
    if f'-{identifier}' in track['slug']:
        print(
            f'This is not a -{identifier} track.  '
            f'Please convert to dev using --identifier {identifier} first.'
        )
        exit(1)

    # Remove identifier from track slug
    track['slug'] = track['slug'].removesuffix(f'-{identifier}')

    # Remove identifier from track title
    track['title'] = track['title'].replace(f'{identifier.upper()} -', '')

    # Remove IDs from assignments.md files
    assignment_paths = glob.glob(
        f'{track_path}/**/assignment.md',
        recursive=True
        )

    # Loop Through Assignments and remove id: key
    for assignment in assignment_paths:
        try:
            with click.open_file(assignment, mode='r') as af_r:
                doc = frontmatter.loads(af_r.read())
                # TODO: Update assignment ID to match instruqt API
                doc.metadata.pop('id', None)
                assignment_output = frontmatter.dumps(doc, sort_keys=False)
                with click.open_file(assignment, mode='w') as af_w:
                    af_w.write(assignment_output)
                    af_w.close()
                af_r.close()

        except FileNotFoundError as assignment_exception:
            print(f'Unable to open {assignment}: {assignment_exception}')
            exit(1)

    # TODO: Update track ID to match instruqt API
    # Remove ID from track.yml
    track.pop('id', None)

    # Dump track.yml
    try:
        with click.open_file(f'{track_path}/track.yml', mode='w') as tf_w:
            # Write file changes
            yaml.dump(track, tf_w, sort_keys=False)
    except PermissionError as update_exception:
        print(f'Unable to write track.yml: {update_exception}')
        exit(1)
