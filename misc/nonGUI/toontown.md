# Toontown

> Source: https://wikipedia.org/wiki/Toontown_Online

> Aliases: toontown-mod, tto, tto-mod

$ Toon
    `~correctlaff()                {{Corrects toon's laff.}} 
    `~nametag(styleName)           {{Set the style of target's nametag.}} 
    `~emotes                       {{Unlock all emote animations on the target toon.}} 
    `~phrase(phraseStringOrId)     {{Unlocks a new phrase and adds it to target's list of their phrases.}} 
    `~setCE(CEValue, CEHood, CEExpire)
>                                  {{Set Cheesy Effect of the target.}} 
    `~setHp(hpVal)                 {{Set target's current laff.}} 
    `~setMaxHp(hpVal)              {{Set target's laff.}} 
    `~maxToon                      {{Max out the toons stats.}} 
    `~setMaxMoney(Amount to be able to hold)
>                                  {{Set target's money and maxMoney values.}} 
    `~setName(name)                {{Set target's name.}} 
    `~setHat(hatId, hatTex=0)      {{Set hat of target toon.}} 
    `~setGlasses(glassesId, glassesTex=0)
>                                  {{Set glasses of target toon.}} 
    `~setBackpack(bpId, bpTex=0)   {{Set backpack of target toon.}} 
    `~setShoes(shoesId, shoesTex=0)
>                                  {{Set shoes of target toon.}} 
    `~togGM()                      {{Toggle GM Icon for toon.}} 
    `~ghost()                      {{Set toon to invisible.}} 
    `~setGM(gmId)                  {{Set the target's GM level (used for icon).}} 
    `~setCogIndex(indexVal)        {{Transform into a cog/suit.}} 
    `~setCogSuit                   {{Set cog suit and level}} 
    `~dna(part, value)             {{Set a specific part of DNA for the target toon.}} 
    `~immortal()                   {{Make target or self immortal.}} 
    `~houseType(type)              {{Set target house type.}} 
    `~setBattleSkip(bs)            {{Skip battle.}} 
    `~sleep                        {{Never fall asleep.}} 

$ Toontasks
    `~setQP(questId, progress)     {{Get current questId in progress via ~setQP. Set questId progress via ~setQP questId value.}} 
    `~questTier(tier)              {{Set toon's tier to specified value.}} 

$ Items
    `~setTrackAccess(gagtrack)     {{Set target's gag track acess.}} 
    `~tracks(gagtrack)             {{Set access for each of the 7 gag tracks. (EX: ~tracks 1 1 0 0 1 1 0)}} 
    `~exp(track, amount)           {{Set your experience to the amount specified for a single track.}} 
    `~merits(corp, amount)         {{Set the target's merits to the value specified.}} 
    `~fanfare()                    {{Give target toon a fanfare.}} 
    `~catalog()                    {{Delivers target's catalog.}} 
    `~pouch(number of gags)        {{Set the target's max gag limit.}} 
    `~givePies(pieType, number of Pies)
>                                  {{Give target Y number of X pies.}} 
    `~unlimitedGags()              {{Restock avatar's gags at the start of each round.}} 
    `~sos(amount)(SOS name)        {{ Gives the player the SOS toon.}} 
    `~goodsos()                    {{Restock all *good* VP SOS toons.}} 
    `~unites()                     {{Restock all CFO phrases.}} 
    `~summons()                    {{Restock all CJ summons.}} 
    `~pinkslips()                  {{Restock (to 99) CEO pink slips.}} 

$ Cogs
    `~invasionstatus               {{Returns the number of cogs available in an invasion.}} 
    `~spawnCog(cog)                {{Spawn cog. Names must use the first letter of each word (ex: The Big Cheese : tbc).}} 
    `~spawnBuilding                {{Spawn a cog building.}} 
    `~spawnFO                      {{Spawn a Field Office (For a lawbot Field Office type ~spawnFO lawbot).}} 
    `~invasion(cmd, name, num, specialSuit)
>                                  {{Spawn an invasion on the current AI if one doesn't exist.}} 
    `~boss(cmd, val, val2)         {{Commands that can be run on the current boss in the invoker's zone.}} 
    `~skipCEO                      {{ Skip a ceo round.}} 
    `~skipVP                       {{Skip a VP round.}} 
    `~skipCJ                       {{Skip a CJ round.}} 
    `~skipCFO                      {{Skip a CFO round.}} 

$ Games
    `~gibfish(fishName)            {{Sets a flag on the avatar, that upon casting a fishing rod (that is valid), gives the avatar the requested fish.}} 
    `~nogibfish                    {{Deletes a request for a fish if it exists.}} 
    `~stopBingo                    {{Stops Fish Bingo.}} 
    `~startBingo                   {{Starts Fish Bingo.}} 
    `~requestBingoCard(cardName, seed)
>                                  {{Send request for bingo card.}} 
    `~setFishingRod(rodVal)        {{Set target's fishing rod value.}} 
    `~setMaxFishTank(tankVal)      {{Set target's max fish tank value.}} 
    `~abortMinigame                {{Abort any minigame you are currently in.}} 
    `~winMinigame                  {{Win the current minigame you are in.}} 
    `~requestMinigame(minigameName, minigameKeep, minigameDiff, minigamePG)
>                                  {{Request a certain trolley game.}} 
    `~setTickets(Amount you want to change to)
>                                  {{Set the target's racing ticket's value.}} 
    `~leaveRace                    {{Leave the current race you are in.}} 
    `~setTrophyScore(value)        {{Set the trophy score of target.}} 
    `~travel(target)               {{Trolley tracks.}} 

$ System
    `~system                       {{Broadcast a message to your entire district.}} 
    `~garbage(arg)                 {{Reports the total garbage use for this process.}} 
    `~heap()                       {{Counts the number of objects in Python's object memory.}} 
    `~objects(minimum)             {{Write the objects down to log.}} 
    `~containers(limit)            {{Write the container report to log.}} 
    `~clickNametag(avId)           {{Simulate a click on an avatar's nametag, given their ID.}} 
    `~showTarget()                 {{Show the moderators current Magic Word target.}} 
    `~accId()                      {{Get the accountId from the target player.}} 
    `~run()                        {{Toggle running, which makes you move much faster.}} 
    `~collisionsOff()              {{Turn off collisions. This allows you to run through things, and walk in air.}} 
    `~collisionsOn()               {{Re-enable collisions.}} 
    `~setGravity(gravityValue, overrideWarning)
>                                  {{Set your gravity value!.}} 
    `~getPos()                     {{Get current position of your toon.}} 
    `~setPos(toonX, toonY, toonZ)  {{Set position of your toon.}} 
    `~chatmode(mode=)              {{Set the chat mode of the current avatar.}} 
    `~oobe()                       {{Toggle out of body experience view.}} 
    `~oobeCull()                   {{Toggle out of body experience view, with culling debugging.}} 
    `~wire()                       {{Toggle wireframe view.}} 
    `~textures()                   {{Toggle textures on and off.}} 
    `~fps()                        {{Toggle frame rate meter on or off.}} 
    `~showAvIds()                  {{Show avId in Nametags.}} 
    `~showNames()                  {{Remove avIds in Nametags.}} 
    `~showAccess()                 {{Show access level.}} 

