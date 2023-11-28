// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.ControlTower
{
    [EnumType]
    public readonly struct LandingZoneDriftStatus : IEquatable<LandingZoneDriftStatus>
    {
        private readonly string _value;

        private LandingZoneDriftStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LandingZoneDriftStatus Drifted { get; } = new LandingZoneDriftStatus("DRIFTED");
        public static LandingZoneDriftStatus InSync { get; } = new LandingZoneDriftStatus("IN_SYNC");

        public static bool operator ==(LandingZoneDriftStatus left, LandingZoneDriftStatus right) => left.Equals(right);
        public static bool operator !=(LandingZoneDriftStatus left, LandingZoneDriftStatus right) => !left.Equals(right);

        public static explicit operator string(LandingZoneDriftStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LandingZoneDriftStatus other && Equals(other);
        public bool Equals(LandingZoneDriftStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct LandingZoneStatus : IEquatable<LandingZoneStatus>
    {
        private readonly string _value;

        private LandingZoneStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LandingZoneStatus Active { get; } = new LandingZoneStatus("ACTIVE");
        public static LandingZoneStatus Processing { get; } = new LandingZoneStatus("PROCESSING");
        public static LandingZoneStatus Failed { get; } = new LandingZoneStatus("FAILED");

        public static bool operator ==(LandingZoneStatus left, LandingZoneStatus right) => left.Equals(right);
        public static bool operator !=(LandingZoneStatus left, LandingZoneStatus right) => !left.Equals(right);

        public static explicit operator string(LandingZoneStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LandingZoneStatus other && Equals(other);
        public bool Equals(LandingZoneStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
