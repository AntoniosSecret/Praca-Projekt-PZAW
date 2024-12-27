const input = document.getElementById("songInput")
const list = document.getElementById('list')
const table = document.getElementById('songTable')
const button = document.getElementById('songButton')
const endBackground = document.getElementById('endBackground')
const endPage = document.getElementById('endPage')
const endButton = document.getElementById('endButton')

const turnLimit = 10
const columns = 4

var turn = 0
var guesses = 0

const albumNames = [
    'The College Dropout',
    'Late Registration',
    'Graduation',
    '808s & Heartbreak',
    'My Beautiful Dark Twisted Fantasy',
    'Watch The Throne',
    'Yeezus',
    'The Life Of Pablo',
    'ye',
    'KIDS SEE GHOSTS',
    'JESUS IS KING',
    'Donda',
    'VULTURES 1',
    'VULTURES 2'
]

const albumImages = [
    'theCollegeDropout',
    'lateRegistration',
    'graduation',
    '808sAndHeartbreak',
    'myBeautifulDarkTwistedFantasy',
    'watchTheThrone',
    'yeezus',
    'theLifeOfPablo',
    'ye',
    'kidsSeeGhosts',
    'jesusIsKing',
    'donda',
    'vultures1',
    'vultures2'
]


fetch('/static/games/json/songs.json').then(response => response.json()).then(data => {
    const songNamesAll = data.songNamesAll
    const songNames = data.songNames

    const randAlbum = Math.floor(Math.random() * songNames.length)
    const randSong = Math.floor(Math.random() * songNames[randAlbum].length)
    const randSongName = songNames[randAlbum][randSong][0]
    const randTime = songNames[randAlbum][randSong][1]
    const randAlbumName = albumNames[randAlbum]
    const randAlbumImage = albumImages[randAlbum]

    var songGuessed = false

    input.addEventListener('input', function() {
        const value = input.value
        list.innerHTML = ''

        if (!value) return

        const filteredSuggestions = songNamesAll.filter(item => 
            item.toLowerCase().startsWith(value.toLowerCase())
        )

        filteredSuggestions.forEach(item => {
            const suggestionItem = document.createElement('div')
            suggestionItem.classList.add('song')
            suggestionItem.textContent = item

            suggestionItem.addEventListener('click', function() {
                input.value = item
                list.innerHTML = ''
            })

            list.appendChild(suggestionItem)
        })
    })

    document.addEventListener('click', function(e) {
        if (e.target !== input) {
            list.innerHTML = ''
        }
    })

    function saveGameState() {
        const state = {
            turn,
            guesses,
            tableHTML: table.innerHTML,
            inputPlaceholder: input.placeholder,
            songGuessed,
            randAlbum,
            randSong,
            randSongName,
            randTime,
            randAlbumName,
            randAlbumImage,
        }
        sessionStorage.setItem('gameState', JSON.stringify(state))
    }
    
    function restoreGameState() {
        const savedState = sessionStorage.getItem('gameState')
        if (savedState) {
            const {
                turn: savedTurn,
                guesses: savedGuesses,
                tableHTML, inputPlaceholder,
                songGuessed: savedSongGuessed,
                randAlbum: savedRandAlbum,
                randSong: savedRandSong,
                randSongName: savedRandSongName,
                randTime: savedRandTime,
                randAlbumName: savedRandAlbumName,
                randAlbumImage: savedRandAlbumImage,
            } = JSON.parse(savedState)
            turn = savedTurn
            guesses = savedGuesses
            table.innerHTML = tableHTML
            input.placeholder = inputPlaceholder || `Próba ${guesses + 1}/10`
            songGuessed = savedSongGuessed || false
            
            randAlbum = savedRandAlbum
            randSong = savedRandSong
            randSongName = savedRandSongName
            randTime = savedRandTime
            randAlbumName = savedRandAlbumName
            randAlbumImage = savedRandAlbumImage
    
            if (songGuessed || guesses >= 10) {
                endGame(songGuessed)
            }
        }
    }
    
    restoreGameState()
    

    button.addEventListener('click', () => {
        if (turn > turnLimit) return

        const value = input.value
        input.value = ''
        

        if (songNamesAll.includes(value)) {
            guesses++
            input.placeholder = `Próba ${guesses+1}/10`
            for (var album = 0; album < songNames.length; album++) {
                for (var song = 0; song < songNames[album].length; song++) {
                    let k = songNames[album][song].indexOf(value)
                    if (k == 0) {
                        var selAlbumName = albumNames[album]
                        var selAlbumImage = albumImages[album]
                        var selAlbumPos = album
                        
                        var selSongName = songNames[album][song][0]
                        var selSongLen = songNames[album][song][1]
                        var selSongPos = song

                        createTr()
                    }
                }
            }

            function createTr() {
                var newTr = document.createElement('tr')

                for (let i = 0; i < columns; i++) {
                    var newTd = document.createElement('td')

                    if (i == 0) {
                        newTd.textContent = selSongName

                        if (randSong == selSongPos && randAlbum == selAlbumPos) {
                            songGuessed = true
                            newTd.style.backgroundColor = "rgb(59, 134, 63)"
                        }
                    }
                    else if (i == 1) {
                        newTd.className = 'imageBox'
                        var image = document.createElement('img')

                        image.src = `/static/games/yeezle-images/${selAlbumImage}.png`
                        image.alt = selAlbumName

                        newTd.appendChild(document.createTextNode(" "))
                        let arrowSpan = document.createElement("span")
                        arrowSpan.className = "arrow"

                        if (randAlbum > selAlbumPos) {
                            arrowSpan.textContent = "▲"
                        }
                        else if (randAlbum < selAlbumPos) {
                            arrowSpan.textContent = "▼"
                        }
                        if (Math.abs(randAlbum-selAlbumPos) <= 2 && randAlbum != selAlbumPos) {
                            newTd.style.backgroundColor = "rgb(184, 157, 82)"
                        }
                        else if (randAlbum == selAlbumPos) {
                            newTd.style.backgroundColor = "rgb(59, 134, 63)"
                        }

                        newTd.appendChild(image)
                        newTd.appendChild(arrowSpan)
                    }
                    else if (i == 2) {
                        newTd.textContent = selSongPos + 1
                        newTd.appendChild(document.createTextNode(" "))
                        let arrowSpanSong = document.createElement("span")
                        arrowSpanSong.className = "arrow"
                        if (randSong > selSongPos) {
                            arrowSpanSong.textContent = "▲"
                        }
                        else if (randSong < selSongPos) {
                            arrowSpanSong.textContent = "▼"
                        }
                        if (Math.abs(randSong-selSongPos) <= 2 && randSong != selSongPos) {
                            newTd.style.backgroundColor = "rgb(184, 157, 82)"
                        }
                        else if (randSong == selSongPos) {
                            newTd.style.backgroundColor = "rgb(59, 134, 63)"
                        }
                        newTd.appendChild(arrowSpanSong)
                    }
                    else if (i == 3) {
                        newTd.textContent = selSongLen

                        let timeSelectedConvert = selSongLen.split(":")
                        let trueSelectedTime = (parseInt(timeSelectedConvert[0])*60)+parseInt(timeSelectedConvert[1])

                        let timeRandConvert = randTime.split(":")
                        let trueRandTime = (parseInt(timeRandConvert[0])*60)+parseInt(timeRandConvert[1])

                        newTd.appendChild(document.createTextNode(" "))

                        let arrowSpanTime = document.createElement("span")
                        arrowSpanTime.className = "arrow"

                        if (trueRandTime > trueSelectedTime)
                            arrowSpanTime.textContent = "▲"
                        else if (trueRandTime < trueSelectedTime)
                            arrowSpanTime.textContent = "▼"

                        if (Math.abs(trueRandTime-trueSelectedTime) <= 30 && trueRandTime != trueSelectedTime)
                            newTd.style.backgroundColor = "rgb(184, 157, 82)"
                        else if (trueRandTime == trueSelectedTime)
                            newTd.style.backgroundColor = "rgb(59, 134, 63)"

                        newTd.appendChild(arrowSpanTime)
                    }

                    newTr.appendChild(newTd)
                }
                table.appendChild(newTr)

                saveGameState()

                if (songGuessed) {
                    endGame(songGuessed)
                }
                if (guesses >= 10) {
                    input.placeholder = "Guess 10/10"
                    endGame(songGuessed)
                }
            }

            function endGame(result) {
                endBackground.style.display = 'block'

                var status = document.createElement('p')

                var span = document.createElement('span')
                span.innerHTML = 'Piosenką było:'

                var image = document.createElement('img')
                image.src = `/static/games/yeezle-images/${randAlbumImage}.png`
                image.alt = randAlbumName

                var song = document.createElement('h1')
                song.innerHTML = randSongName

                if (result) {
                    status.innerHTML = 'Wygrałeś'
                }
                else {
                    status.innerHTML = 'Przegrałeś'
                }

                endPage.appendChild(status)
                endPage.appendChild(span)
                endPage.appendChild(image)
                endPage.appendChild(song)

                saveGameState()
            }
        }
    })
})

endButton.addEventListener('click', () => {
    endBackground.style.display = 'none'
    sessionStorage.clear()
})