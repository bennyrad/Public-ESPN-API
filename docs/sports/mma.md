# 🥊 MMA

> Mixed Martial Arts from the UFC, Bellator, and dozens of international promotions.

**Sport slug:** `mma`  
**Base URL (v2):** `http://sports.core.api.espn.com/v2/sports/mma/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/mma/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `ACB` | Absolute Championship Berkut | `absolute` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/absolute` |
| `AFFLICTION` | Affliction | `affliction` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/affliction` |
| `BFC` | Bang Fighting Championships | `bang-fighting` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/bang-fighting` |
| `BFC` | Banni Fight Combat | `banni-fight` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/banni-fight` |
| `BFC` | Banzay Fight Championship | `banzay` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/banzay` |
| `BFC` | Barracao Fight Championship | `barracao` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/barracao` |
| `BFC` | Battlezone Fighting Championships | `battlezone` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/battlezone` |
| `BFC` | Bellator Fighting Championship | `bellator` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/bellator` |
| `BFC` | Benevides Fight Championship | `benevides` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/benevides` |
| `BFC` | Big Fight Champions | `big-fight` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/big-fight` |
| `BFC` | Blackout Fighting Championship | `blackout` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/blackout` |
| `BFC` | Bosnia Fight Championship | `bosnia` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/bosnia` |
| `BFC` | Boxe Fight Combat | `boxe` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/boxe` |
| `BFC` | Brazilian Freestyle Circuit | `brazilian-freestyle` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/brazilian-freestyle` |
| `BFC` | Budo Fighting Championships | `budo` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/budo` |
| `CWFC` | Cage Warriors Fighting Championship | `cage-warriors` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/cage-warriors` |
| `DREAM` | Dream | `dream` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/dream` |
| `FNG` | Fight Nights Global | `fng` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/fng` |
| `IFC` | Invicta FC | `ifc` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/ifc` |
| `IFL` | International Fight League | `ifl` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/ifl` |
| `K-1` | K-1 | `k1` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/k1` |
| `KSW` | Konfrontacja Sztuk Walki | `ksw` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/ksw` |
| `LFA` | Legacy Fighting Alliance | `lfa` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/lfa` |
| `LFC` | Legacy Fighting Championship | `lfc` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/lfc` |
| `M-1` | M-1 Mix-Fight Championship | `m1` | `http://sports.core.api.espn.com/v2/sports/mma/leagues/m1` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `http://sports.core.api.espn.com/v2/sports/mma/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

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
# List leagues for MMA
curl "http://sports.core.api.espn.com/v2/sports/mma/leagues"

# Get Absolute Championship Berkut teams
curl "http://sports.core.api.espn.com/v2/sports/mma/leagues/absolute/teams"

# Get current season events
curl "http://sports.core.api.espn.com/v2/sports/mma/leagues/absolute/events"

# Get athletes (players)
curl "http://sports.core.api.espn.com/v2/sports/mma/leagues/absolute/athletes"

# Get standings
curl "http://sports.core.api.espn.com/v2/sports/mma/leagues/absolute/standings"
```