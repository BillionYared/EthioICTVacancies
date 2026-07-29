# Ethiopia ICT Vacancy Telegram Bot

A zero-server-cost vacancy tracker for Ethiopian ICT internships and junior roles. It searches the web, scores relevant results, avoids duplicates, and sends new matches to Telegram.

## Tracks

- ICT / IT support internships
- Linux and systems administration
- Network and NOC internships
- Infrastructure and data-center support
- Cloud support and DevOps trainee roles
- Information systems and digital technology internships

It prioritizes searches for UNECA, UNOPS, African Union, ILRI, UNICEF, UNDP, IOM, WFP, GIZ, international NGOs, banks, telecoms, ISPs, and Ethiopian vacancy sites.

## Free-hosting design

GitHub Actions runs the scanner three times each day. There is no continuously running server. Scheduled jobs may start late, so this is intended for vacancy alerts, not real-time chat.

## 1. Create the Telegram bot

1. Open Telegram and message `@BotFather`.
2. Send `/newbot` and follow the instructions.
3. Copy the bot token.
4. Start a private chat with your new bot and send `/start`.
5. Obtain your numeric chat ID by opening:

   `https://api.telegram.org/botYOUR_TOKEN/getUpdates`

   Find `message.chat.id` in the response.

For a channel, add the bot as an administrator and set `TELEGRAM_CHAT_ID` to the public username such as `@EthioICTVacancies`, or use the numeric channel ID.

## 2. Upload to GitHub

Create a new GitHub repository and upload every file in this project, including the `.github` folder.

## 3. Add repository secrets

Open:

`Repository → Settings → Secrets and variables → Actions → New repository secret`

Create:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Never put the token directly in the code.

## 4. Test it

Open:

`Actions → Ethiopia ICT Vacancy Watch → Run workflow`

Enable **Send a Telegram connection test** for the first run.

## 5. Schedule

The included workflow scans at approximately:

- 08:17 Ethiopia time
- 14:17 Ethiopia time
- 20:17 Ethiopia time

GitHub scheduled workflows use UTC and can be delayed. Change the cron values in `.github/workflows/vacancy-watch.yml` when needed.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

Set environment variables and run:

```bash
export TELEGRAM_BOT_TOKEN='your-token'
export TELEGRAM_CHAT_ID='your-chat-id'
python main.py
```

PowerShell:

```powershell
$env:TELEGRAM_BOT_TOKEN='your-token'
$env:TELEGRAM_CHAT_ID='your-chat-id'
python main.py
```

## Customize searches

Edit `app/config.py`:

- `SEARCH_QUERIES` controls searches.
- `POSITIVE_TERMS` controls technical relevance.
- `ENTRY_TERMS` identifies internship/junior roles.
- `SENIOR_TERMS` suppresses experienced roles.
- `PRIORITY_DOMAINS` boosts trusted job sites.

## Limitations

- Search engines can occasionally throttle or change results.
- A result may be old even when newly indexed; always verify the date and deadline.
- Some sites block search engines or require login.
- GitHub Actions is not an always-on Telegram command bot.
- The bot does not apply for jobs automatically.

## Recommended future upgrades

- Add an admin approval queue before publishing to a public channel.
- Add a small web dashboard.
- Add source-specific parsers for organizations that post frequently.
- Add subscriber preferences by skill and location using a hosted database.
