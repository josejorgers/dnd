# D&D with LLM

This program allows you to play Dungeons and Dragons (D&D) using Python, with the assistance of an LLM (Large Language Model), all packaged within a Docker container.

## Features

* Text-based Gameplay: Engage in immersive text-based adventures with the assistance of the LLM.
* Character Creation: Create and customize your own characters for your D&D adventures.
* Dynamic Storytelling: Experience dynamic storytelling, where the plot unfolds based on your decisions and actions.
* Dice Rolling: Utilize dice rolling mechanics to determine the outcome of actions and encounters.
* Flexible Gameplay: Play solo or with friends, with the LLM acting as the Dungeon Master (DM) to guide you through your adventures.

## Requirements

* Docker

## Setup

* Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/dnd-with-llm-python.git
```

* Navigate to the project directory:

```bash
cd dnd-with-llm-python
```
* Create a ```.env``` file with the following content:
  ```
  OPENAI_API_KEY=<your api key>
  ```
* Build the Docker image:

```bash
Copy code
docker build -t dnd-with-llm .
```

* Run the Docker container:

```bash
docker run -it dnd-with-llm
```

Follow the prompts to create your character and start your adventure.

>**Note:** If you use Linux and can use `make`, you can substitute the previous docker build and run commands with `make build` and `make run` instead

You have also a dockerized development environment defined in `Dockerfile.dev`.

>**Note:** Make commands for building and running the development environment are: `make build-dev` and `make run-dev`.

Enjoy your D&D adventure with the assistance of the LLM acting as the Dungeon Master!

## Contributing

Contributions to this project are welcome! Whether you want to add new features, improve existing functionality, or implement your own version, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
