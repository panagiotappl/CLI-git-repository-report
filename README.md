# Git repository report

A git analyzer that produces beautiful and readable statistics for a git repo in HTML format.
This project has been developed for the needs of the "Software Engineering" course of the University of Athens.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

This is a CLI tool.
To run the python version pass two parameters. The first one is the path of the github repo
and the second is the destination directory for the output.

```
python ./src/cli.py <repo_dir_path> <output_dir_path>
```

To run the jvm version:

```
java -jar cli-git.jar <repo_dir_path> <output_dir_path>
```

## Built With

* [Jython](http://www.jython.org/) - Python on JVM.
* [D3pie](http://d3pie.org/) - Simple, attractive pie charts.
* [AmCharts](https://www.amcharts.com) - JavaScript Charts & Maps.

## Contributing

Feel free to contribute by cloning this project and submitting a pull request.

## Authors

* **Panagiota Poulopoulou** - *University of Athens*
* **Panos Paparrigopoulos** - *University of Athens*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Explanation

You can see the  [Explanation.md](explanation.md) for details on stats calculation and other info.
