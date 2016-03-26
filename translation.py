import textblob

def translate_to_converge(in_text, max_iter):
    c_text = textblob.TextBlob(in_text)
    for i in range(0,max_iter):
        n_text = c_text.translate(from_lang='en', to='la')
        n_text = n_text.translate(from_lang='la', to='el')
        n_text = n_text.translate(from_lang='el', to='iw')
        n_text = n_text.translate(from_lang='iw', to='el')
        n_text = n_text.translate(from_lang='el', to='la')
        n_text = n_text.translate(from_lang='la', to='en')

        #print('%s vs %s'%(c_text, n_text))
        if c_text == n_text:
            return '%s'%(n_text)
        c_text = n_text

    return '%s'%(n_text)

if __name__ == '__main__':
    #var = raw_input("Please enter something: ")
    input = 'The reward for humility is the fear of the Lord, riches and honor and life'
    output = translate_to_converge(input, 10)
    print('started with: %s'%(input))
    print('ended with: %s'%(output))

