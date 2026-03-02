# ⚾ Baseball

> Baseball from Major League Baseball (MLB), college, winter leagues, and international tournaments.

**Sport slug:** `baseball`  
**Base URL (v2):** `http://sports.core.api.espn.com/v2/sports/baseball/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/baseball/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `CBWS` | Caribbean Series | `caribbean-series` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/caribbean-series` |
| `CBASE` | NCAA Baseball | `college-baseball` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/college-baseball` |
| `CSOFT` | NCAA Softball | `college-softball` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/college-softball` |
| `DOMWL` | Dominican Winter League | `dominican-winter-league` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/dominican-winter-league` |
| `LITTLE LEAGUE BASEBALL WORLD SERIES` | Little League Baseball | `llb` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/llb` |
| `LITTLE LEAGUE SOFTBALL WORLD SERIES` | Little League Softball | `lls` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/lls` |
| `LMB` | Mexican League | `mexican-winter-league` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/mexican-winter-league` |
| `MLB` | Major League Baseball | `mlb` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb` |
| `OLYBB` | Olympics Men's Baseball | `olympics-baseball` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/olympics-baseball` |
| `PUERT` | Puerto Rican Winter League | `puerto-rican-winter-league` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/puerto-rican-winter-league` |
| `VENWL` | Venezuelan Winter League | `venezuelan-winter-league` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/venezuelan-winter-league` |
| `WBBC` | World Baseball Classic | `world-baseball-classic` | `http://sports.core.api.espn.com/v2/sports/baseball/leagues/world-baseball-classic` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

---

## V3 Endpoints

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v3/sports/{sport}/athletes` | `getAthletes` | `page`, `limit`, `_hoist`, `_help`, `_trace`, `_nocache`, `enable`, `disable`, `pq`, `q`, `page`, `limit`, `lang`, `region`, `utcOffset`, `dates`, `weeks`, `advance`, `event.recurring`, `ids`, `type`, `types`, `seasontypes`, `calendar.type`, `calendar.groups`, `status`, `statuses`, `groups`, `provider`, `provider.priority`, `site`, `league.type`, `split`, `splits`, `record.splits`, `record.seasontype`, `statistic.splits`, `statistic.seasontype`, `statistic.qualified`, `statistic.context`, `sort`, `roster.positions`, `roster.athletes`, `team.athletes`, `powerindex.rundatetimekey`, `eventsback`, `eventsforward`, `eventsrange`, `eventstates`, `eventresults`, `seek`, `tournaments`, `competitions`, `competition.types`, `teams`, `situation.play`, `oldteams`, `newteams`, `played`, `period`, `position`, `filter`, `available`, `active`, `ids.sportware`, `profile`, `opponent`, `eventId`, `homeAway`, `season`, `athlete.position`, `postalCode`, `award.type`, `notes.type`, `tidbit.type`, `networks`, `bets.promotion`, `guids`, `competitors`, `source` |
| `https://sports.core.api.espn.com/v3/sports/{sport}/{league}` | `getLeague` | `page`, `limit`, `_hoist`, `_help`, `_trace`, `_nocache`, `enable`, `disable`, `pq`, `q`, `page`, `limit`, `lang`, `region`, `utcOffset`, `dates`, `weeks`, `advance`, `event.recurring`, `ids`, `type`, `types`, `seasontypes`, `calendar.type`, `calendar.groups`, `status`, `statuses`, `groups`, `provider`, `provider.priority`, `site`, `league.type`, `split`, `splits`, `record.splits`, `record.seasontype`, `statistic.splits`, `statistic.seasontype`, `statistic.qualified`, `statistic.context`, `sort`, `roster.positions`, `roster.athletes`, `team.athletes`, `powerindex.rundatetimekey`, `eventsback`, `eventsforward`, `eventsrange`, `eventstates`, `eventresults`, `seek`, `tournaments`, `competitions`, `competition.types`, `teams`, `situation.play`, `oldteams`, `newteams`, `played`, `period`, `position`, `filter`, `available`, `active`, `ids.sportware`, `profile`, `opponent`, `eventId`, `homeAway`, `season`, `athlete.position`, `postalCode`, `award.type`, `notes.type`, `tidbit.type`, `networks`, `bets.promotion`, `guids`, `competitors`, `source` |
| `https://sports.core.api.espn.com/v3/sports/{sport}/{league}/seasons/{season}` | `getSeason` | `page`, `limit`, `_hoist`, `_help`, `_trace`, `_nocache`, `enable`, `disable`, `pq`, `q`, `page`, `limit`, `lang`, `region`, `utcOffset`, `dates`, `weeks`, `advance`, `event.recurring`, `ids`, `type`, `types`, `seasontypes`, `calendar.type`, `calendar.groups`, `status`, `statuses`, `groups`, `provider`, `provider.priority`, `site`, `league.type`, `split`, `splits`, `record.splits`, `record.seasontype`, `statistic.splits`, `statistic.seasontype`, `statistic.qualified`, `statistic.context`, `sort`, `roster.positions`, `roster.athletes`, `team.athletes`, `powerindex.rundatetimekey`, `eventsback`, `eventsforward`, `eventsrange`, `eventstates`, `eventresults`, `seek`, `tournaments`, `competitions`, `competition.types`, `teams`, `situation.play`, `oldteams`, `newteams`, `played`, `period`, `position`, `filter`, `available`, `active`, `ids.sportware`, `profile`, `opponent`, `eventId`, `homeAway`, `season`, `athlete.position`, `postalCode`, `award.type`, `notes.type`, `tidbit.type`, `networks`, `bets.promotion`, `guids`, `competitors`, `source` |

---

## Example API Calls

```bash
# List leagues for Baseball
curl "http://sports.core.api.espn.com/v2/sports/baseball/leagues"

# Get Caribbean Series teams
curl "http://sports.core.api.espn.com/v2/sports/baseball/leagues/caribbean-series/teams"

# Get current season events
curl "http://sports.core.api.espn.com/v2/sports/baseball/leagues/caribbean-series/events"

# Get athletes (players)
curl "http://sports.core.api.espn.com/v2/sports/baseball/leagues/caribbean-series/athletes"

# Get standings
curl "http://sports.core.api.espn.com/v2/sports/baseball/leagues/caribbean-series/standings"
```