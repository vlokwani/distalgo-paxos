Answer 1)
    i)  As per the paper 'Paxos made Simple, we consider a scenario in which multiple proposers     keep sending a sequence of new proposals with increasing numbers because of which none      of them are chosen. Let's assume proposer P receives promise(phase 1b) for a proposal       number n1. Another proposer Q then sends a prepare and receives a promise for a             proposal number n2 where n2 > n1. Proposer P accept requests for a proposal numbered n1     will then be ignored because the acceptors would have promised Q not to accept any new      proposal numbered less than n2. So, Proposer P will begin and complete the first phase      for a new proposal number n3 > n2, causing the phase 2 accept request of proposer Q to      be ignored which will cause the system to never progress.
    
    ii) To guarantee progress, the paper suggests that we can elect a distinguished proposer        can be selected and only this proposer is only one allowed to try issuing of proposals.     If the leader can communicate successfully with a majority of acceptors, for a proposal     with proposal number greater than the onle already used, then it will succeed in            issuing a proposal that gets accepted. By dropping the proposal and trying again if it
        learns about some request with a higher proposal number, the distinguished proposer will eventually succeed in establishing concensus in the system.

Answer 2) 
    i)  
    
    a) Storing messages for slots that are no longer required. 
    
    First, note that although a leader obtains for each slot a set of all accepted pvalues
    from a majority of acceptors, it only needs to know if this set is empty or not, and if not what the maximum pvalue is. Thus, a large step toward practicality is that acceptors only maintain the most recently accepted pvalue for each slot (⊥ if no pvalue has been accepted) and return only these pvalues in a p1b message to the scout. This gives the leader all information needed to enforce Invariant C2.

    b) 