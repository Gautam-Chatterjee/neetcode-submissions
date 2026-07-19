class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    

    def find(self,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    

    def union(self, p1,p2):
        p1, p2 = self.find(p1), self.find(p2)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}

        for i,a in enumerate(accounts):
            for email in a[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        
        emailGroup = defaultdict(list)

        for email,i in email_to_acc.items():
            parent_account = uf.find(i)
            emailGroup[parent_account].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res





        