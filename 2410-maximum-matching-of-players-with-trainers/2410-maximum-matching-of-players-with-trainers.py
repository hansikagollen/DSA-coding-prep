class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        count=0
        i=j=0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                #match found
                count+=1
                i+=1
                j+=1
            else:
                #try next trainer
                j+=1

        return count
        