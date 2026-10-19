# HomeLab-as-Code

[![ci](https://github.com/BebinTailan/HomeLab-as-Code/actions/workflows/ci.yml/badge.svg)](https://github.com/BebinTailan/HomeLab-as-Code/actions/workflows/ci.yml)

HomeLab-as-Code describes a lab network (sites, VLANs, subnets, routers, links, security zones) in a
single TOML file, validates it, and generates everything needed to build and document it: IP plan,
diagrams, containerlab topology, FRRouting OSPF configs, nftables rulesets, WireGuard templates and a
connectivity test plan.

> **Status:** early development. See [docs/ROADMAP.md](docs/ROADMAP.md).

## Requirements

- Python 3.11+ (uses the standard `tomllib`)
- To actually run the generated lab: Linux or WSL2 with Docker and containerlab (optional)

## Usage

```bash
python -m homelab --version
```

## Development

```bash
python -m unittest discover -s tests -v
```

## Security

No secret is ever stored in this repository. VPN keys and lab passwords are generated on the
machine that deploys the lab.
