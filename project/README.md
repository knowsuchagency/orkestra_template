
# Welcome to your Orkestra project

## Requirements

<details>
<summary>Install <a href="https://pdm.fming.dev">PDM</a> and <a href="https://copier.readthedocs.io/en/latest/">Copier</a></summary>

```bash
brew install pipx
pipx install pdm
pipx install copier
```

</details>

<details>
<summary>Install <a href="https://docs.aws.amazon.com/cdk/latest/guide/cli.html">CDK</a></a></summary>

```bash
npm install -g aws-cdk
```

</details>


## Usage

```bash
# copy template
copier ...

# install library dependencies
pdm install

# deploy
pdm run deploy
```

## Notes

Any environment variables you want to set for commands you invoke via `pdm run {{command}}` can be configured in your
`.env` file.

Just be sure to add `.env` to your `.gitignore` if adding secrets.
