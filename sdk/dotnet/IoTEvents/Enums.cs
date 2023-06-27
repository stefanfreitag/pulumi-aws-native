// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.IoTEvents
{
    /// <summary>
    /// The comparison operator.
    /// </summary>
    [EnumType]
    public readonly struct AlarmModelSimpleRuleComparisonOperator : IEquatable<AlarmModelSimpleRuleComparisonOperator>
    {
        private readonly string _value;

        private AlarmModelSimpleRuleComparisonOperator(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AlarmModelSimpleRuleComparisonOperator Greater { get; } = new AlarmModelSimpleRuleComparisonOperator("GREATER");
        public static AlarmModelSimpleRuleComparisonOperator GreaterOrEqual { get; } = new AlarmModelSimpleRuleComparisonOperator("GREATER_OR_EQUAL");
        public static AlarmModelSimpleRuleComparisonOperator Less { get; } = new AlarmModelSimpleRuleComparisonOperator("LESS");
        public static AlarmModelSimpleRuleComparisonOperator LessOrEqual { get; } = new AlarmModelSimpleRuleComparisonOperator("LESS_OR_EQUAL");
        public static AlarmModelSimpleRuleComparisonOperator Equal { get; } = new AlarmModelSimpleRuleComparisonOperator("EQUAL");
        public static AlarmModelSimpleRuleComparisonOperator NotEqual { get; } = new AlarmModelSimpleRuleComparisonOperator("NOT_EQUAL");

        public static bool operator ==(AlarmModelSimpleRuleComparisonOperator left, AlarmModelSimpleRuleComparisonOperator right) => left.Equals(right);
        public static bool operator !=(AlarmModelSimpleRuleComparisonOperator left, AlarmModelSimpleRuleComparisonOperator right) => !left.Equals(right);

        public static explicit operator string(AlarmModelSimpleRuleComparisonOperator value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AlarmModelSimpleRuleComparisonOperator other && Equals(other);
        public bool Equals(AlarmModelSimpleRuleComparisonOperator other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Information about the order in which events are evaluated and how actions are executed.
    /// </summary>
    [EnumType]
    public readonly struct DetectorModelEvaluationMethod : IEquatable<DetectorModelEvaluationMethod>
    {
        private readonly string _value;

        private DetectorModelEvaluationMethod(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorModelEvaluationMethod Batch { get; } = new DetectorModelEvaluationMethod("BATCH");
        public static DetectorModelEvaluationMethod Serial { get; } = new DetectorModelEvaluationMethod("SERIAL");

        public static bool operator ==(DetectorModelEvaluationMethod left, DetectorModelEvaluationMethod right) => left.Equals(right);
        public static bool operator !=(DetectorModelEvaluationMethod left, DetectorModelEvaluationMethod right) => !left.Equals(right);

        public static explicit operator string(DetectorModelEvaluationMethod value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorModelEvaluationMethod other && Equals(other);
        public bool Equals(DetectorModelEvaluationMethod other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
