# 🎍 Plaza

#### Social media built for the future.

<p align="center">
  <a title="Codefactor" target="_blank" href="https://github.com/RiversideValley/Plaza/commits">
    <img align="left" src="https://www.codefactor.io/repository/github/RiversideValley/Plaza/badge" alt="CodeFactor" />
  </a>
  <a title="Build" target="_blank" href="https://github.com/RiversideValley/Plaza/actions/workflows/build-image.yml">
    <img align="left" src="https://github.com/RiversideValley/Plaza/actions/workflows/build-image.yml/badge.svg" alt="Build" />
  </a>
  <a title="Javascript" target="_blank" href="https://github.com/RiversideValley/Plaza/actions/workflows/test-js.yml">
    <img align="left" src="https://github.com/RiversideValley/Plaza/actions/workflows/test-js.yml/badge.svg" alt="Javascript" />
  </a>
  <a title="SCSS" target="_blank" href="https://github.com/RiversideValley/Plaza/actions/workflows/lint-css.yml">
    <img align="left" src="https://github.com/RiversideValley/Plaza/actions/workflows/lint-css.yml/badge.svg" alt="SCSS" />
  </a>
</p>

<br/>
<br/>

<p align="center">
  <a title="Why is ActivityPub the future?" target="_blank" href="https://www.youtube.com/watch?v=IPSbNdBmWKE">
    <img src="https://blog.joinmastodon.org/2018/06/why-activitypub-is-the-future/ezgif-2-60f1b00403.gif" alt="Why is ActivityPub the future?" />
  </a>
</p>

---

<!--## 🎁 Create an account

### Via desktop app
###### ⭐Recommended⭐

[`download`](https://apps.microsoft.com)
[`sideload`](https://github.com/RiversideValley/Plaza/releases)

### Via webapp

[protocol interconnect](https://andrexial.org.uk/auth/sign_up)

### Via android app

[`sideload`](https://github.com/RiversideValley/Plaza/releases)-->

<!--## 📸 Screenshots

<a title="Emerald Screenshot" target="_blank" href="https://github.com/RiversideValley/Plaza">
  <img align="left" src="https://user-images.githubusercontent.com/82730163/210150183-fd324c12-5a90-4ffb-964d-c8ccae2c9cee.png" alt="Release" />
</a>-->

## 🪪 Hosting details

#### Hosted in London.

Currently hosted on `riverside` Hyperactive servers (yes, Riverside Valley _does_ have servers) in **London, UK**.
Unit used is the most high-end model of Raspberry Pi, running Ubuntu.

###### 📝 Earlier versions were hosted in **Cleveland, USA** (via `vercel`) or **Southern UK** and operated via an interface server in the **Netherlands** (via `azure`).

## 🦜 Contributing & feedback

There are multiple ways to participate in the community:

- Upvote popular feature requests
- [Submit a new feature](https://github.com/RiversideValley/Plaza/pulls)
- [File bugs and feature requests](https://github.com/RiversideValley/Plaza/issues/new/choose).
- Review source [code changes](https://github.com/RiversideValley/Plaza/commits)

## 🏗️ Codebase Structure

```c
.
├──.circleci                         // CircleCI configuration for building Plaza pipeline (disused)
├──.devcontainer                     // Scripts and preparation files for running Plaza in a development container such as github.dev
├──.github                           // Health files for GitHub such as issue templates
├──app                               // Collection of code files relating to the app's frontend
├──bin                               // Scripts for running and hosting Plaza
├──config                            // Code files relating to federated hosting and Ruby bootstrappers
├──db                                // Database files for Plaza's information database (Host-specific backend; reserved for Plaza hosting)
├──dist                              // Collection of code files relating app hosting on domains and port relations
├──lib                               // Code and file library
├──log                               // Hosting logs (Host-specific backend; reserved for Plaza hosting)
├──public                            // Static resource files
├──spec                              // Helpers, presenters, and other code models
├──streaming                         // (Host-specific backend; reserved for Plaza hosting)
└──vendor                            // (Host-specific backend; reserved for Plaza hosting)
```

## ⚖️ License

Copyright (c) 2023 Riverside Valley Corporation (+ [`mastodon authors`](https://github.com/mastodon/mastodon/blob/main/AUTHORS.md))

Licensed under GNU Affero General Public License as stated in the [LICENSE](LICENSE.md):

```

Copyright (C) 2016-2022 Eugen Rochko & other Mastodon contributors

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see https://www.gnu.org/licenses/.

```
