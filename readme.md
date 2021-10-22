# Incooom Genesis Traits Scraper

Crude python script which uses Infura to interact with the chain and scrapes the Incooom genesis card trait data, and creates a simple SQL script for use in Dune. This resulted in the following PR https://github.com/duneanalytics/abstractions/pull/494 (though I should really correct my typo in that PR)

Requires the environment variable `WEB3_INFURA_PROJECT_ID` to be set. 