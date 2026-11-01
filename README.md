# superagent-playground

A small repository used to try out [dsh-superagent](https://github.com/deepseek-ai/dsh-superagent-prototype)
end to end: a request arrives as an issue comment, the agent opens a work item,
works in its own directory, and delivers a pull request.

## Layout

- `greet.py` — a tiny module with room for improvement (no tests, ASCII-only behaviour).

## Running

```sh
python3 -c "from greet import greet; print(greet('world'))"
```
