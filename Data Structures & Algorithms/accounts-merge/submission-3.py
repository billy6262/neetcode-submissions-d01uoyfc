class UF:
    def __init__(self,n):
        self.nodes = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node) -> int:
        while self.nodes[node] != node:
            self.nodes[node] =  self.nodes[self.nodes[node]]
            node = self.nodes[node]
        return node

    def union(self,n1,n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.nodes[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.nodes[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        emailtoacc = dict()


        for ai, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailtoacc:
                    uf.union(ai, emailtoacc[email])
                else:
                    emailtoacc[email] = ai

        ufaccounts = defaultdict(list)
        for e , i in emailtoacc.items():
            main = uf.find(i)
            ufaccounts[main].append(e)

        arr = []
        for root_idx, emails in ufaccounts.items():
            arr.append([accounts[root_idx][0]] + sorted(emails))

        return arr
