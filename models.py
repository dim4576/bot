class ExecutorModel():

    def __init__(self, chat_id=0, name=0, sity=0, number=0, wish=False):
        self.id = chat_id
        self.name = name
        self.sity = sity
        self.number = number
        self.wish = wish
        self.part = None

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getSity(self):
        return self.sity

    def getNumber(self):
        return self.number

    def getWish(self):
        return self.wish

    def getPart(self):
        return self.part

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setSity(self, sity):
        self.sity = sity

    def setNumber(self, number):
        self.number = number

    def setWish(self, wish):
        self.wish = wish

    def setPart(self, part):
        self.part = part

    def print(self):
        i = self
        print('part: {} id: {} number: {} name: {} sity: {} wish: {}'.format(i.getPart(), i.getId(), i.getNumber(), i.getName(), i.getSity(), i.getWish()))


class ExecutorsModel():
    def __init__(self):
        self.exs = []

    def len(self):
        return len(self.exs)

    def search_id(self, id):
        for i in self.exs:
            if id == i.getId():
                return i.getPart()

    def add(self, executor):
        if self.search_id(executor.getId()) is None:
            part = self.len()
            executor.setPart(part)
            self.exs.append(executor)

    def remove(self, part):
        del(self.exs[part])
        print('remoxe: ok')

    def remove_id(self, id):
        self.remove(self.search_id(id))

    def search_sity(self, sity):
        res = ExecutorsModel()
        for i in self.exs:
            if sity == i.getSity():
                res.add(i)
        return res

    def search_wish(self):
        res = ExecutorsModel()
        for i in self.exs:
            if i.getWish():
                res.add(i)
        return res

    def getUnit(self, part):
        if part != None:
            return self.exs[part]

    def print(self):
        if self.len() == 0:
            print('list is empty')
            return
        for i in self.exs:
            print('part: {} id: {} number: {} name: {} sity: {} wish: {}'.format(i.getPart(), i.getId(), i.getNumber(), i.getName(), i.getSity(), i.getWish()))

def main():
    import pickle
    try:
        with open('base.db', 'rb') as f:
            base = pickle.load(f)
    except Exception:
        base = ExecutorsModel()
        with open('base.db', 'wb') as f:
            pickle.dump(base, f)

    while True:

        unit = ExecutorModel()
        comand = input('enter the comand: ')
        if comand == '+':
            unit.setId(int(input('enter a chat id: ')))
            unit.setNumber(input('enter a number: '))
            unit.setName(input('enter a name: '))
            unit.setSity(input('enter a sity: '))
            wish = input('enter a wish(y/n): ')
            if wish == 'y': unit.setWish(True)
            elif wish == 'n': unit.setWish(False)
            base.add(unit)
            with open('base.db', 'wb') as f:
                pickle.dump(base, f)
        elif comand == 'print':
            try:
                with open('base.db', 'rb') as f:
                    base = pickle.load(f)
            except Exception:
                base = ExecutorsModel()
                with open('base.db', 'wb') as f:
                    pickle.dump(base, f)
            base.print()

        elif 'remove' in comand.split():
            base.remove(int(comand.split()[1]))
            with open('base.db', 'wb') as f:
                pickle.dump(base, f)

        elif comand == 'stop':
            try:
                with open('base.db', 'rb') as f:
                    base = pickle.load(f)
            except Exception:
                base = ExecutorsModel()
                with open('base.db', 'wb') as f:
                    pickle.dump(base, f)
            break
        else: print('error: ankown command!!!')


    print('==============================================================')
    print('full list:')
    base.print()
    print('==============================================================')
    print('list of units finded on sity Vitebsk:')
    base.search_sity('vitebsk').print()
    print('==============================================================')
    print('wont in work of him:')
    base.search_sity('vitebsk').search_wish().print()
    print('==============================================================')
    print('unit with id = 111 this:')
    k = base.getUnit(base.search_id(111))
    if k != None:
        k.print()
    else: print('unit with id 111 not found')



if __name__ == '__main__':
    main()
