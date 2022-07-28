# instruqt-converter

Python based CLI tool to convert Instruqt (<https://www.instruqt.com>) tracks to and from a temporary state for testing.  This tool utilizes the Instruqt GraphQL API to validate tracks and use existing track and challenge IDs if available.

## Configuration

Before using the tool you will need to do the following:

### Install instruqt-converter

```shell
pip install instruqt-converter
```

### Configure Environment Variables

```shell
cp ENVEXAMPLE ~/.instruqt-converter.env
```

After you have copied `ENVEXAMPLE` to `~/.instruqt-converter.env` update the following key/value pairs:

* `INSTRUQT_API_KEY` - Replace `<api-key>` with the API key from your Instruqt team settings page

* `INSTRUQT_ORG_SLUG` - Replace `<org-slug>` with your organizations slug

Load the environment variables:

```shell
source ~/.instruqt-converter.env
```

You may want to add `source ~/.instruqt-converter.env` to your shell profile so the environment variables are loaded every time you log in.

## Usage

### Help

```shell
vscode ➜ /workspaces/development/instruqt-converter $ convert --help

 Usage: convert [OPTIONS]

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  *  --track         PATH        Path to Instruqt track [required]                                                                                    │
│  *  --to            [dev|prod]  Convert To: [dev] - Convert to dev for testing [prod] - Convert to prod for promotion [required]                     │
│  *  --identifier    TEXT        Track identifier used when converting to dev [default: dev] [required]                                               │
│     --help                      Show this message and exit.                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Converting to Dev Track

```shell
vscode ➜ /workspaces/development/instruqt-converter (main ✗) $ convert --track /workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible --to dev
[21:41:23] INFO     Converting to [dev] with identifier [dev]                                                                                                                                                     convert.py:56
[21:41:24] WARNING  Track with identifier: [dev] and ID: vbiz8rpaul3w already exists.                                                                                                                                 dev.py:50
           WARNING  Found Existing Assignment [explore-the-environment] with ID: 3swpbta9acpw                                                                                                                         dev.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/01-explore-the-environment/assignment.md]                                         dev.py:103
           WARNING  Found Existing Assignment [configure-system] with ID: lp2ahqitimsf                                                                                                                                dev.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/02-configure-system/assignment.md]                                                dev.py:103
           WARNING  Found Existing Assignment [configure-ntp] with ID: 4ju8kkouqiug                                                                                                                                   dev.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/03-configure-ntp/assignment.md]                                                   dev.py:103
           WARNING  Found Existing Assignment [configure-snmp] with ID: ywddqrez9r38                                                                                                                                  dev.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/04-configure-snmp/assignment.md]                                                  dev.py:103
           WARNING  Found Existing Assignment [configure-interfaces] with ID: q1z7o0lg7hpm                                                                                                                            dev.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/05-configure-interfaces/assignment.md]                                            dev.py:103
           WARNING  Found Existing Assignment [configure-ospf] with ID: kmf8zc84x83o                                                                                                                                  dev.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/06-configure-ospf/assignment.md]                                                  dev.py:103
           INFO     Setting id in track.yml to: vbiz8rpaul3w                                                                                                                                                         dev.py:121
           INFO     Completed update of /workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/track.yml                                                                          dev.py:141
           INFO     Track conversion to [dev] with identifier [dev] complete!                                                                                                                                        dev.py:142
```

### Converting to Prod Track

```shell
vscode ➜ /workspaces/development/instruqt-converter (main ✗) $ convert --track /workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible --to prod
[21:42:20] INFO     Converting to [prod] with identifier [dev]                                                                                                                                                    convert.py:60
[21:42:21] WARNING  Track with identifier: [dev] and ID: zcr4yrnk5jgr already exists.                                                                                                                                prod.py:50
           WARNING  Found Existing Assignment [explore-the-environment] with ID: puhvtzr2iij2                                                                                                                        prod.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/01-explore-the-environment/assignment.md]                                        prod.py:103
           WARNING  Found Existing Assignment [configure-system] with ID: dlxrwky2yfb7                                                                                                                               prod.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/02-configure-system/assignment.md]                                               prod.py:103
           WARNING  Found Existing Assignment [configure-ntp] with ID: qvj2hx3kj1q4                                                                                                                                  prod.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/03-configure-ntp/assignment.md]                                                  prod.py:103
           WARNING  Found Existing Assignment [configure-snmp] with ID: m8lal25bbcqe                                                                                                                                 prod.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/04-configure-snmp/assignment.md]                                                 prod.py:103
           WARNING  Found Existing Assignment [configure-interfaces] with ID: pin7dorfav3y                                                                                                                           prod.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/05-configure-interfaces/assignment.md]                                           prod.py:103
           WARNING  Found Existing Assignment [configure-ospf] with ID: n7t3cuwcd9vg                                                                                                                                 prod.py:74
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/06-configure-ospf/assignment.md]                                                 prod.py:103
           INFO     Setting id in track.yml to: zcr4yrnk5jgr                                                                                                                                                        prod.py:121
           INFO     Completed update of /workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/track.yml                                                                         prod.py:141
           INFO     Track conversion to [prod] with identifier [dev] complete!                                                                                                                                      prod.py:142
```

### Using a different track identifier

The tool also supports using track identifiers other than `dev`.  To change the identifier use the `--identifier` command line option.

```shell
vscode ➜ /workspaces/development/instruqt-converter (main ✗) $ convert --track /workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible --to dev --identifier nick
[21:58:22] INFO     Converting to [dev] with identifier [nick]                                                                                                                                                    convert.py:56
[21:58:23] ERROR    Track with identifier: nick does not exist                                                                                                                                                        dev.py:57
           INFO     Assignment [explore-the-environment] does not exist  Removing id.                                                                                                                                 dev.py:88
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/01-explore-the-environment/assignment.md]                                         dev.py:103
           INFO     Assignment [configure-system] does not exist  Removing id.                                                                                                                                        dev.py:88
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/02-configure-system/assignment.md]                                                dev.py:103
           INFO     Assignment [configure-ntp] does not exist  Removing id.                                                                                                                                           dev.py:88
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/03-configure-ntp/assignment.md]                                                   dev.py:103
           INFO     Assignment [configure-snmp] does not exist  Removing id.                                                                                                                                          dev.py:88
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/04-configure-snmp/assignment.md]                                                  dev.py:103
           INFO     Assignment [configure-interfaces] does not exist  Removing id.                                                                                                                                    dev.py:88
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/05-configure-interfaces/assignment.md]                                            dev.py:103
           INFO     Assignment [configure-ospf] does not exist  Removing id.                                                                                                                                          dev.py:88
           INFO     Completed update of [/workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/06-configure-ospf/assignment.md]                                                  dev.py:103
           INFO     Track [network-automation-challenge-lab-nick] not found.  Removing id.                                                                                                                           dev.py:128
           INFO     Completed update of /workspaces/development/network-automation-challenge-lab/instruqt-challenge-cisco-ansible/track.yml                                                                          dev.py:141
           INFO     Track conversion to [dev] with identifier [nick] complete!
```

## Version

Version: v0.0.1-beta.5

## Changelog

See `CHANGELOG.md` for changes.

## Contributors

* Nick Thompson ([@nsthompson](https://github.com/nsthompson))
