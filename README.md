# Repository Statistics
This program analyzes all of the repositories within `repos` (not included due to size). 

## Structure
`data` holds text files generated by the analyzer

	`stats-per-repo` is all of the metrics of typed vs untyped assignments & functions within each repository

	`typed-repos` is a list of all repositories that use atleast 1 type in their python code

`micro-data` holds statistics based on the `test-cases/micro-cases`

`test-cases` holds a bunch of hand-written test cases for analysis

`tools` holds all of the tooling for analysis + documentation