from faker import Faker
import random

fake = Faker()

def generate_basketball_data(num_teams=16, num_players_per_team=10):
    teams = []
    coaches = []
    players = []

    for _ in range(num_teams):
        team_name = fake.company() + " Basketball Team"
        coach_name = fake.name()
        teams.append(team_name)
        coaches.append(coach_name)
        
        team_players = []
        for _ in range(num_players_per_team):
            player_name = fake.name()
            player_height = round(random.uniform(1.70, 2.10), 2)
            team_players.append((player_name, player_height))
        
        players.append(team_players)
    
    return teams, coaches, players


teams, coaches, players = generate_basketball_data()


for i in range(len(teams)):
    print(f"Team {i+1}: {teams[i]}")
    print(f"Coach: {coaches[i]}")
    print("Players:")
    for player in players[i]:
        print(f" - {player[0]}, Height: {player[1]}m")
    print("\n")


#Data generated:

"""
Team 1: Pacheco Basketball Team
Coach: Margaret Hughes
Players:
 - Chad Hall, Height: 1.71m
 - Matthew Acosta, Height: 1.97m
 - Andrew Morris, Height: 2.07m
 - Tony White, Height: 1.96m
 - Todd May, Height: 1.79m
 - Robert Taylor, Height: 2.04m
 - John Campbell, Height: 1.85m
 - Carolyn Jones, Height: 2.06m
 - Christopher Knight, Height: 1.73m
 - Gina Jacobs, Height: 1.89m


Team 2: Bennett Basketball Team
Coach: Stephanie Gallegos DDS
Players:
 - Charles Brown, Height: 1.7m
 - Joshua Ford, Height: 1.93m
 - Ashley Lawrence, Height: 1.94m
 - Brianna Walsh, Height: 1.9m
 - Christopher Frazier, Height: 2.02m
 - Amy Allen, Height: 2.04m
 - Robert Harris, Height: 1.88m
 - Andrew Quinn, Height: 1.86m
 - Nancy Murphy, Height: 1.98m
 - Tabitha Thomas, Height: 1.87m


Team 3: Russell Basketball Team
Coach: Scott Davis
Players:
 - Annette Mosley, Height: 1.91m
 - Joseph Lynn, Height: 2.01m
 - William Guerrero, Height: 1.82m
 - Cristian Espinoza, Height: 1.75m
 - April Lee, Height: 1.83m
 - Kyle Scott, Height: 1.77m
 - Angela Navarro, Height: 1.93m
 - Bradley Henry, Height: 2.02m
 - Kristopher Gonzalez, Height: 2.06m
 - Steven Thompson, Height: 1.71m


Team 4: Welch Basketball Team
Coach: John Olson
Players:
 - Alexis Hartman, Height: 1.96m
 - Gabriela Hicks, Height: 1.82m
 - Tracy Day, Height: 1.88m
 - Christine Horn, Height: 1.71m
 - Sally Harrison, Height: 1.76m
 - Donald Alexander, Height: 2.06m
 - John Williams, Height: 1.71m
 - Lonnie Dillon, Height: 1.79m
 - Randy Kirby, Height: 2.04m
 - Jason Williams MD, Height: 1.89m


Team 5: Thornton Basketball Team
Coach: Charles Kelly
Players:
 - James Ortega, Height: 1.92m
 - Christopher Mercer, Height: 1.91m
 - Erica Johnson, Height: 1.81m
 - Miranda Pennington, Height: 1.77m
 - Ashlee Simmons, Height: 2.04m
 - Tammy Johnson, Height: 2.06m
 - Jacob Lynch, Height: 1.84m
 - Richard Dixon, Height: 1.71m
 - Daniel Curtis, Height: 1.95m
 - Christopher Ramirez, Height: 1.82m


Team 6: Guzman Basketball Team
Coach: David Morgan DDS
Players:
 - Gilbert Leblanc, Height: 1.93m
 - William Bryant, Height: 1.72m
 - Brian Chase, Height: 1.78m
 - Jeanne Reid, Height: 1.79m
 - Brian Stevens, Height: 2.08m
 - Natalie Snyder MD, Height: 1.71m
 - Lisa Beck, Height: 1.75m
 - Donald Allen, Height: 2.05m
 - Sabrina Sullivan, Height: 1.81m
 - Angel Gordon, Height: 1.91m


Team 7: Cummings Basketball Team
Coach: Kristin Morgan MD
Players:
 - Wendy Jordan, Height: 1.89m
 - Suzanne Chang, Height: 1.78m
 - Cynthia Swanson, Height: 1.78m
 - Briana Carney, Height: 1.82m
 - Mary Nicholson, Height: 1.8m
 - Hannah Hamilton, Height: 1.95m
 - Shannon Myers, Height: 1.79m
 - Mr. Justin Williamson, Height: 1.9m
 - Jennifer Joseph, Height: 2.0m
 - Jeffery Evans, Height: 2.0m


Team 8: Thomas Basketball Team
Coach: Mark Gray
Players:
 - Paul Adkins, Height: 2.03m
 - Justin Lee, Height: 1.93m
 - Sandra Chavez, Height: 1.71m
 - Katherine Oneal, Height: 2.06m
 - Chelsea Barnes, Height: 1.75m
 - Melanie Rhodes, Height: 1.97m
 - Jamie Sandoval, Height: 1.7m
 - Linda Davis, Height: 1.82m
 - Molly Elliott, Height: 1.79m
 - Latoya Finley, Height: 1.84m


Team 9: Knight Basketball Team
Coach: Frank Martinez
Players:
 - Cassandra Chandler, Height: 1.71m
 - Connie Ryan, Height: 1.96m
 - Kenneth Davis Jr., Height: 1.74m
 - James Miller, Height: 2.0m
 - Denise Brown, Height: 2.06m
 - Brandon Brown, Height: 2.04m
 - Kathy Harris, Height: 1.97m
 - Christopher Spencer, Height: 1.88m
 - Wendy Davis, Height: 1.83m
 - Brenda Booker, Height: 1.83m


Team 10: Wilson Basketball Team
Coach: Richard Long
Players:
 - Lindsey Osborn, Height: 2.09m
 - James Lewis, Height: 2.05m
 - Gerald Ray, Height: 1.89m
 - Alexander Johnson, Height: 2.05m
 - Thomas Brown, Height: 1.9m
 - Debbie Doyle, Height: 1.78m
 - David Howard, Height: 1.77m
 - Cassie Andrews, Height: 1.84m
 - Cameron Hawkins, Height: 2.08m
 - Courtney Williams, Height: 1.75m


Team 11: Sanders Basketball Team
Coach: Amanda Allison
Players:
 - Dr. Jonathan Baldwin, Height: 1.73m
 - Lisa Lin, Height: 2.0m
 - Daniel Brown, Height: 1.78m
 - Brian Wood, Height: 2.07m
 - Crystal Smith, Height: 1.76m
 - Laura Lamb, Height: 1.74m
 - Kevin Shepard, Height: 1.92m
 - Wendy Smith, Height: 1.84m
 - Alexandra Sims, Height: 1.8m
 - Tiffany Hall, Height: 1.75m


Team 12: Cooke Basketball Team
Coach: Michael Zuniga
Players:
 - Timothy Ewing, Height: 1.74m
 - Ronald Figueroa, Height: 1.81m
 - Gerald Sanchez, Height: 1.86m
 - Aaron Brooks, Height: 1.77m
 - Bryan Johnson, Height: 1.84m
 - Shane Bailey, Height: 1.97m
 - Ms. Jessica Ross, Height: 1.95m
 - James Booth, Height: 2.02m
 - Yolanda Jennings, Height: 1.77m
 - Christopher Morales, Height: 2.0m


Team 13: Ross Basketball Team
Coach: Christine Lopez
Players:
 - Sydney Bridges, Height: 1.85m
 - Jacqueline Cook, Height: 2.07m
 - Megan Ramirez, Height: 1.9m
 - Kevin Spencer PhD, Height: 2.08m
 - Robert Mason, Height: 1.76m
 - James Wall, Height: 1.72m
 - Helen Davis, Height: 2.08m
 - Katie Hicks, Height: 2.0m
 - Melinda Contreras, Height: 1.85m
 - Michael Calderon, Height: 2.02m


Team 14: Hunter Basketball Team
Coach: Michelle Miller
Players:
 - Mckenzie Arnold, Height: 1.77m
 - Angel Gallagher, Height: 1.94m
 - Brandon Rangel, Height: 1.75m
 - Jeremy Ball, Height: 1.7m
 - Steve Scott, Height: 1.73m
 - Deborah Ramirez, Height: 1.74m
 - Margaret Gonzalez, Height: 1.91m
 - Amanda Hill, Height: 2.06m
 - Timothy Becker, Height: 1.84m
 - Jessica Mathews, Height: 1.91m


Team 15: Gonzalez Group Basketball Team
Coach: Alan Clark
Players:
 - Craig Fitzpatrick, Height: 1.86m
 - Anthony Rowe, Height: 2.07m
 - Luis Randolph, Height: 1.9m
 - Lisa Roach, Height: 1.74m
 - Shelley Smith, Height: 1.81m
 - Matthew Gilmore, Height: 1.77m
 - Dana Davidson, Height: 1.99m
 - Judith Meza, Height: 1.95m
 - Allison Hamilton, Height: 1.85m
 - Mrs. Chelsea Villegas, Height: 2.05m


Team 16: Clark Basketball Team
Coach: Candice Holmes
Players:
 - David Smith, Height: 1.95m
 - Maria Young, Height: 1.85m
 - Jennifer Armstrong, Height: 2.04m
 - Sean Caldwell, Height: 2.03m
 - Colleen Scott, Height: 1.72m
 - Jennifer Barton, Height: 1.95m
 - Kevin Villarreal, Height: 1.82m
 - Christopher Thompson, Height: 1.77m
 - Barry Gonzalez, Height: 1.89m
 - Manuel Hicks, Height: 1.99m

"""