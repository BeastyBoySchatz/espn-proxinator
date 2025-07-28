from flask import Flask, request, jsonify
from espn_api.football import League

app = Flask(__name__)

@app.route("/my-team", methods=["GET"])
def get_my_team():
    league_id = request.args.get("leagueId")
    team_id = int(request.args.get("teamId"))
    swid = request.args.get("swid")
    espn_s2 = request.args.get("espn_s2")

    try:
        league = League(
            league_id=league_id,
            year=2024,
            espn_s2=espn_s2,
            swid=swid
        )
        team = next(t for t in league.teams if t.team_id == team_id)
        data = {
            "team_name": team.team_name,
            "roster": [player.name for player in team.roster],
            "record": team.standing
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

app.run(host='0.0.0.0', port=8080)

