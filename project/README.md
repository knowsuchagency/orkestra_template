
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

### environment variables

Any environment variables you want to set for commands you invoke via `pdm run {{command}}` can be configured in your
`.env` file.

### bootstrapping

If this is the first time there's been a CDK deployment into the AWS account you're deploying to, the account may need
to be bootstrapped.

The full documentation on that process is here: https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html

```bash
pdm run cdk bootstrap
```
