package com.example.unscramble.ui

import com.example.unscramble.data.MAX_NO_OF_WORDS

import org.junit.Assert.*
import org.junit.Before
import org.junit.Test

class GameViewModelTest {

    private lateinit var viewModel: GameViewModel

    @Before
    fun setup() {
        viewModel = GameViewModel()
    }

    @Test
    fun initialState_isCorrect() {
        val state = viewModel.uiState.value
        assertEquals(1, state.currentWordCount)
        assertEquals(0, state.score)
        assertFalse(state.isGuessedWordWrong)
        assertFalse(state.isGameOver)
        assertTrue(state.currentScrambledWord.isNotBlank())
        assertEquals("", viewModel.userGuess)
    }

    @Test
    fun updateUserGuess_updatesGuess() {
        viewModel.updateUserGuess("test")
        assertEquals("test", viewModel.userGuess)
    }

    @Test
    fun skipWord_incrementsWordCountWithoutChangingScore() {
        val before = viewModel.uiState.value
        viewModel.skipWord()
        val after = viewModel.uiState.value

        assertEquals(before.score, after.score)
        assertEquals(before.currentWordCount + 1, after.currentWordCount)
        assertFalse(after.isGuessedWordWrong)
        assertEquals("", viewModel.userGuess)
    }

    @Test
    fun skipWord_changesScrambledWord() {
        val before = viewModel.uiState.value.currentScrambledWord
        viewModel.skipWord()
        val after = viewModel.uiState.value.currentScrambledWord

        assertNotEquals(before, after)
    }

    @Test
    fun checkUserGuess_wrongGuess_setsErrorFlag() {
        viewModel.updateUserGuess("___точно_неправильное_слово___")
        viewModel.checkUserGuess()

        val state = viewModel.uiState.value
        assertTrue(state.isGuessedWordWrong)
        assertEquals(0, state.score)
        assertEquals(1, state.currentWordCount)
        assertEquals("", viewModel.userGuess)
    }

    @Test
    fun checkUserGuess_correctGuess_increasesScore() {
        // здесь нужен способ узнать правильное слово — см. ниже
    }

    @Test
    fun gameOver_afterMaxSkips() {
        repeat(MAX_NO_OF_WORDS) { viewModel.skipWord() }
        assertTrue(viewModel.uiState.value.isGameOver)
    }

    @Test
    fun resetGame_resetsState() {
        repeat(MAX_NO_OF_WORDS) { viewModel.skipWord() }
        viewModel.resetGame()

        val state = viewModel.uiState.value
        assertFalse(state.isGameOver)
        assertEquals(0, state.score)
        assertEquals(1, state.currentWordCount)
        assertFalse(state.isGuessedWordWrong)
    }
}