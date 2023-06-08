# Changelog

## [1.2.0](https://github.com/CHIMEFRB/skaha/compare/v1.1.1...v1.2.0) (2023-06-08)


### Features

* **client:** updated client to include skaha version in prep for v1 release ([e6360c0](https://github.com/CHIMEFRB/skaha/commit/e6360c07d9b305463e00f2f8293e6c9a2dc83f42))
* **overview:** added new overview module ([4a6336f](https://github.com/CHIMEFRB/skaha/commit/4a6336ff9d1ff3e05701848a500d35585cb0b154))


### Bug Fixes

* **deps:** updates ([5644e15](https://github.com/CHIMEFRB/skaha/commit/5644e15c5b28de2a54be2607d87ca2a3439e7659))
* **session:** fix for spawning sessions with gpus ([961f766](https://github.com/CHIMEFRB/skaha/commit/961f76673783f948a6cf0c3c2b70bb34e4d6d853))
* **tests:** fixed session tests, which now default spawn with name-{replica-id} format ([7e48031](https://github.com/CHIMEFRB/skaha/commit/7e48031281e5ed1e35b891655769977aa4d3fc44))

## [1.1.1](https://github.com/CHIMEFRB/skaha/compare/v1.1.0...v1.1.1) (2022-12-16)


### Documentation

* **readme:** update ([1b975b6](https://github.com/CHIMEFRB/skaha/commit/1b975b67da82a68d8c5072cc5739dcd024f39584))

## [1.1.0](https://github.com/CHIMEFRB/skaha/compare/v1.0.2...v1.1.0) (2022-12-16)


### Features

* **docs:** added build ([9049b92](https://github.com/CHIMEFRB/skaha/commit/9049b92b211bf4081b07f397a1c62ce058f3183b))
* **session:** create session now embeds two env variables into the container, REPLICA_COUNT and REPLICA_ID ([ecbf48a](https://github.com/CHIMEFRB/skaha/commit/ecbf48ad19536945f2359e75d0c3482a2e77feee))


### Bug Fixes

* **docs:** build command issue ([becbc60](https://github.com/CHIMEFRB/skaha/commit/becbc60fb605dd832a90b6b5e5941ce07dc092b6))
* **docs:** fixed build issue ([98b0543](https://github.com/CHIMEFRB/skaha/commit/98b0543f933087cac63955c40dd424285f70656f))

## [1.0.2](https://github.com/CHIMEFRB/skaha/compare/v1.0.1...v1.0.2) (2022-12-15)


### Bug Fixes

* **docs:** created documentation for the project ([e0f5483](https://github.com/CHIMEFRB/skaha/commit/e0f5483c2c72cd489258a84e3cb06d142a06f4da))


### Documentation

* **API-Reference:** changed where order of docs ([569d34f](https://github.com/CHIMEFRB/skaha/commit/569d34f00747fd1d2eff8f997ae277b63080df50))

## [1.0.1](https://github.com/CHIMEFRB/skaha/compare/v1.0.0...v1.0.1) (2022-12-15)


### Bug Fixes

* **env:** fixed multiple tests and added support for multiple env parameters ([c0500bf](https://github.com/CHIMEFRB/skaha/commit/c0500bf9c49a359f0b45205a5d1d6524144940f1))

## [1.0.0](https://github.com/CHIMEFRB/skaha/compare/v0.5.0...v1.0.0) (2022-12-14)


### ⚠ BREAKING CHANGES

* **session:** this is a signficant change, breaking all backwards compatibility
* **sessions:** skaha sessions api is no longer supported, the capability to manage multiple sessions is now provided by default with the skaha.session api itself

### Features

* **session:** added support for multiple session management ([219b74c](https://github.com/CHIMEFRB/skaha/commit/219b74cefc99264aca8f041a625dea30325c1f0d))
* **sessions:** skaha.sessions api deprecated ([e184663](https://github.com/CHIMEFRB/skaha/commit/e18466330e67a1b714da86062c79710fd459fa39))


### Bug Fixes

* **client:** updated session header to have the correct content-type ([3146e41](https://github.com/CHIMEFRB/skaha/commit/3146e418b6e075edcd5e34dd03e5b94879b17c08))
* **images:** images api now always prunes ([a436e21](https://github.com/CHIMEFRB/skaha/commit/a436e21085f00e5f6e5a408b1ff0bc486c6881f4))
* **pre-commit:** fixed broken pre-commit config ([baedb82](https://github.com/CHIMEFRB/skaha/commit/baedb825a63efca35573d064836b0928e2579029))
* **type-hints:** fixed broken hints ([9f4e9db](https://github.com/CHIMEFRB/skaha/commit/9f4e9dbba8a923d19e5e180f291c7ff216db9c64))
* **type-hints:** fixed broken type hints ([c1d1356](https://github.com/CHIMEFRB/skaha/commit/c1d1356bbba6642bb86e12b1aaf553094e83ea04))

## [0.5.0](https://github.com/CHIMEFRB/skaha/compare/v0.4.1...v0.5.0) (2022-12-14)


### Features

* **release-please:** implemented ([2ac9728](https://github.com/CHIMEFRB/skaha/commit/2ac972870d84876a74c7631f8af5cad453fab81e))


### Bug Fixes

* **gha:** fix to release action ([cc7b61a](https://github.com/CHIMEFRB/skaha/commit/cc7b61a472da50463f3159aac46f6aa3ae49e79c))
