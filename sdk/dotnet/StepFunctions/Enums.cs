// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.StepFunctions
{
    /// <summary>
    /// The type of deployment to perform.
    /// </summary>
    [EnumType]
    public readonly struct StateMachineAliasDeploymentPreferenceType : IEquatable<StateMachineAliasDeploymentPreferenceType>
    {
        private readonly string _value;

        private StateMachineAliasDeploymentPreferenceType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StateMachineAliasDeploymentPreferenceType Linear { get; } = new StateMachineAliasDeploymentPreferenceType("LINEAR");
        public static StateMachineAliasDeploymentPreferenceType AllAtOnce { get; } = new StateMachineAliasDeploymentPreferenceType("ALL_AT_ONCE");
        public static StateMachineAliasDeploymentPreferenceType Canary { get; } = new StateMachineAliasDeploymentPreferenceType("CANARY");

        public static bool operator ==(StateMachineAliasDeploymentPreferenceType left, StateMachineAliasDeploymentPreferenceType right) => left.Equals(right);
        public static bool operator !=(StateMachineAliasDeploymentPreferenceType left, StateMachineAliasDeploymentPreferenceType right) => !left.Equals(right);

        public static explicit operator string(StateMachineAliasDeploymentPreferenceType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StateMachineAliasDeploymentPreferenceType other && Equals(other);
        public bool Equals(StateMachineAliasDeploymentPreferenceType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct StateMachineLoggingConfigurationLevel : IEquatable<StateMachineLoggingConfigurationLevel>
    {
        private readonly string _value;

        private StateMachineLoggingConfigurationLevel(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StateMachineLoggingConfigurationLevel All { get; } = new StateMachineLoggingConfigurationLevel("ALL");
        public static StateMachineLoggingConfigurationLevel Error { get; } = new StateMachineLoggingConfigurationLevel("ERROR");
        public static StateMachineLoggingConfigurationLevel Fatal { get; } = new StateMachineLoggingConfigurationLevel("FATAL");
        public static StateMachineLoggingConfigurationLevel Off { get; } = new StateMachineLoggingConfigurationLevel("OFF");

        public static bool operator ==(StateMachineLoggingConfigurationLevel left, StateMachineLoggingConfigurationLevel right) => left.Equals(right);
        public static bool operator !=(StateMachineLoggingConfigurationLevel left, StateMachineLoggingConfigurationLevel right) => !left.Equals(right);

        public static explicit operator string(StateMachineLoggingConfigurationLevel value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StateMachineLoggingConfigurationLevel other && Equals(other);
        public bool Equals(StateMachineLoggingConfigurationLevel other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct StateMachineType : IEquatable<StateMachineType>
    {
        private readonly string _value;

        private StateMachineType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StateMachineType Standard { get; } = new StateMachineType("STANDARD");
        public static StateMachineType Express { get; } = new StateMachineType("EXPRESS");

        public static bool operator ==(StateMachineType left, StateMachineType right) => left.Equals(right);
        public static bool operator !=(StateMachineType left, StateMachineType right) => !left.Equals(right);

        public static explicit operator string(StateMachineType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StateMachineType other && Equals(other);
        public bool Equals(StateMachineType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
