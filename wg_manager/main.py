def main():
    import sys
    from wg_manager.commands import runner
    runner.run(sys.argv[1:])

if __name__ == "__main__":
    main()
