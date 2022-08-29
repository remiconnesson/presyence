export interface TestResult {
  successful: boolean;
  status: "Success" | "WrongResult" | "Crash";
}

export interface Success extends TestResult {
  status: "Success";
}

export interface WrongResult extends TestResult {
  status: "WrongResult";
  testrun_output: string;
  assertion_error_message: string;
}

export interface Crash extends TestResult {
  status: "Crash";
  traceback: string;
}

export interface TestDefinition {
  title: string;
  function: string;
  input: string;
  expected_output: string;
}

export interface TestReport {
  test: TestDefinition;
  result: Success | WrongResult | Crash;
}
