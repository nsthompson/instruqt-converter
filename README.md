# instruqt-converter

Python based CLI tool to convert Instruqt (<https://www.instruqt.com>) tracks to and from a temporary state for testing.

## Usage

```shell
vscode ➜ /workspaces/development/instruqt-converter $ python3 convert.py --help
                                                                                                                                                        
 Usage: convert.py [OPTIONS]                                                                                                                            
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  *  --track         PATH        Path to Instruqt track [required]                                                                                    │
│  *  --to            [dev|prod]  Convert To: [dev] - Convert to dev for testing [prod] - Convert to prod for promotion [required]                     │
│  *  --identifier    TEXT        Track identifier used when converting to dev [default: dev] [required]                                               │
│     --help                      Show this message and exit.                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Contributors

* Nick Thompson ([@nsthompson](https://github.com/nsthompson))