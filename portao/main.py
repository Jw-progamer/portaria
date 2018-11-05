from antena import  ReceberSinal

if __name__ == '__main__':
    portao = ReceberSinal(5050)
    portao.start()