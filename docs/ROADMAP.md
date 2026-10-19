# Roadmap

Each feature is developed on its own branch (`feature/NN-slug`) and merged into `main` when complete.

## Milestone v0.2.0: model and validation

- [ ] **01 topology-model**: TOML schema (sites, VLANs, subnets, devices, interfaces, links, zones) loaded into typed dataclasses with clear error messages
- [ ] **02 validation**: overlapping subnets, duplicate VLAN IDs or addresses, gateways outside their subnet, dangling links, interface reuse
- [ ] **03 ip-plan-docs**: Markdown IP plan and VLAN tables plus a Mermaid diagram generated from the model

## Milestone v0.3.0: generators

- [ ] **04 containerlab-generator**: containerlab topology (FRR routers, Linux hosts) from the model
- [ ] **05 ospf-configs**: FRRouting configs per router (interfaces, OSPF areas, passive interfaces)
- [ ] **06 nftables-firewall**: zone-based default-deny nftables rulesets from declared flows
- [ ] **07 wireguard-templates**: site-to-site WireGuard configs with key placeholders and a key-generation script

## Milestone v1.0.0: deploy and verify

- [ ] **08 ansible-deploy**: inventory and playbooks that push the generated configs to lab nodes
- [ ] **09 connectivity-tests**: generated test matrix (allowed and denied flows) and a runner script for the lab
- [ ] **10 example-lab**: complete documented example (two sites, three VLANs, VPN, firewall) under `examples/`
