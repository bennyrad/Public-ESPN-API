# 🏉 Rugby

> Rugby Union encompassing international test matches, Six Nations, World Cup, Premiership, Top 14, and more.

**Sport slug:** `rugby`  
**Base URL (v2):** `http://sports.core.api.espn.com/v2/sports/rugby/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/rugby/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `BRITISH AND IRISH LIONS TOUR` | British and Irish Lions Tour | `268565` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/268565` |
| `RUGBY WORLD CUP` | Rugby World Cup | `164205` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/164205` |
| `SIX NATIONS` | Six Nations | `180659` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/180659` |
| `RUGBY CHAMPIONSHIP` | The Rugby Championship | `244293` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/244293` |
| `EUROPEAN RUGBY CHAMPIONS CUP` | European Rugby Champions Cup | `271937` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/271937` |
| `EUROPEAN RUGBY CHALLENGE CUP` | European Rugby Challenge Cup | `272073` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/272073` |
| `PREM RUGBY` | Gallagher Prem | `267979` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/267979` |
| `UNITED RUGBY CHAMPIONSHIP` | United Rugby Championship | `270557` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/270557` |
| `TOP14` | French Top 14 | `270559` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/270559` |
| `URBA PRIMERA A` | URBA Primera A | `2009` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/2009` |
| `SUPER RUGBY PACIFIC` | Super Rugby Pacific | `242041` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/242041` |
| `SUPER RUGBY AOTEAROA` | Super Rugby Aotearoa | `289271` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289271` |
| `SUPER RUGBY AU` | Super Rugby AU | `289272` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289272` |
| `SUPER RUGBY TRANS-TASMAN` | Super Rugby Trans-Tasman | `289277` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289277` |
| `URBA TOP 12` | URBA Top 12 | `289279` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289279` |
| `CURRIE CUP` | Currie Cup | `270555` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/270555` |
| `NATIONAL PROVENCE CHAMPIONSHIP` | Mitre 10 Cup | `270563` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/270563` |
| `ANGLO-WELSH CUP` | Anglo-Welsh Cup | `236461` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/236461` |
| `2020 TRI NATIONS` | 2020 Tri Nations | `289274` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289274` |
| `—` | Olympic Men's 7s | `282` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/282` |
| `OLYWRS` | Olympic Women's Rugby Sevens | `283` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/283` |
| `WOMEN'S RUGBY WORLD CUP` | Women's Rugby World Cup | `289237` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289237` |
| `MAJOR LEAGUE RUGBY` | Major League Rugby | `289262` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289262` |
| `INTERNATIONAL TEST MATCH` | International Test Match | `289234` | `http://sports.core.api.espn.com/v2/sports/rugby/leagues/289234` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/rugby/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

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
# List leagues for Rugby
curl "http://sports.core.api.espn.com/v2/sports/rugby/leagues"

# Get British and Irish Lions Tour teams
curl "http://sports.core.api.espn.com/v2/sports/rugby/leagues/268565/teams"

# Get current season events
curl "http://sports.core.api.espn.com/v2/sports/rugby/leagues/268565/events"

# Get athletes (players)
curl "http://sports.core.api.espn.com/v2/sports/rugby/leagues/268565/athletes"

# Get standings
curl "http://sports.core.api.espn.com/v2/sports/rugby/leagues/268565/standings"
```