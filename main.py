def get_duck_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Setelah kita memanggil perintah bebek (dog), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)