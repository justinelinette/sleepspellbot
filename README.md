<!-- template: https://github.com/othneildrew/Best-README-Template/ -->


<div align="center">
  <a name="readme-top"></a>

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  
  </br>
  <a href="https://github.com/justinelinette/sleepspellbot">
    <img src="https://images2.imgbox.com/be/44/Ep4jsVGZ_o.png" alt="Logo" width="250" height="250">
  </a>

<h1 align="center">sleep spell bot</h3>
  
  the sleep spell discord bot calculates the enemies affected by dnd’s sleep spell, wrapped up conveniently in a bot that can be called right inside your discord server. its intended use is to allow the DM to privately call the bot, provide the sleep spell’s damage, and the hp of all enemies targeted, calculate the effects (ie. who is awake and who is asleep) according to dnd 5e’s rules as written.
</div>

## bot invite link:
<div align="center">
  <h3>
    <u>
      <a href="https://discord.com/api/oauth2/authorize?client_id=1082665111505883146&permissions=534723947584&scope=bot">click here to invite sleep spell bot to your discord server</a>
    </u>
  </h3>
</div>

## installation:



* ensure that you’re signed into a discord account with ‘Manage Server’ privileges for the server to which you’d like to add sleep spell bot
* follow the above link to invite the bot to your server
* select the correct server from the dropdown
* ensure all permissions are checked before clicking ‘Authorize’
* that’s it! the bot should now appear as a member of your server and can be called
    * if using private channels, ensure the bot is added to these channels via ‘Edit Channel’ → ‘Permissions’


## commands:



### !sleep
* the DM should first use the command “!sleep” to call the bot in a private server - keep those enemy hp’s private from your players!
* the bot will then ask for the total sleep damage, to be entered as a simple number, ie. “26”
* the bot will then ask for the hp of each enemy, separated by commas ie. “12, 4, 8”
    * don’t worry about putting the hp’s in order of smallest to least as the written spell demands- we take care of all that for you!
* the bot will then provide the results of the sleep spell in any channel you set using the !response command, so any players can see 
    
### !response
* to set the channel that the bot will drop results in, simply use the command “!response” followed by the name of the channel ie. “!response general”
* the bot will then respond in the channel you’ve set, acknowledging that you’ve successfully changed the response channel


## examples:
<div align="center">
  <a href="https://images2.imgbox.com/b9/dc/2KWVbJnA_o.png">
    <img src="https://images2.imgbox.com/b9/dc/2KWVbJnA_o.png">
  </a>
</div>

## license
distributed under creative commons
see `LICENSE.txt` for more information

## contact

justinelinette - [@punishedgarage](https://twitter.com/punishedgarage)
project link: [https://github.com/justinelinette/sleepspellbot](https://github.com/justinelinette/sleepspellbot)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


[discordpy-shield]: https://img.shields.io/badge/discord--py-ffffff?style=for-the-badge&logo=discord
[discordpy-url]: https://discordpy.readthedocs.io/
[contributors-shield]: https://img.shields.io/github/contributors/justinelinette/sleepspellbot.svg?style=for-the-badge
[contributors-url]: https://github.com/justinelinette/sleepspellbot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/justinelinette/sleepspellbot.svg?style=for-the-badge
[forks-url]: https://github.com/justinelinette/sleepspellbot/network/members
[stars-shield]: https://img.shields.io/github/stars/justinelinette/sleepspellbot.svg?style=for-the-badge
[stars-url]: https://github.com/justinelinette/sleepspellbot/stargazers
[issues-shield]: https://img.shields.io/github/issues/justinelinette/sleepspellbot.svg?style=for-the-badge
[issues-url]: https://github.com/justinelinette/sleepspellbot/issues
[license-shield]: https://img.shields.io/github/license/justinelinette/sleepspellbot.svg?style=for-the-badge
[license-url]: https://github.com/justinelinette/sleepspellbot/blob/master/LICENSE.txt
