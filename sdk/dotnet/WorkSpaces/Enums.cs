// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.WorkSpaces
{
    [EnumType]
    public readonly struct ConnectionAliasConnectionAliasAssociationAssociationStatus : IEquatable<ConnectionAliasConnectionAliasAssociationAssociationStatus>
    {
        private readonly string _value;

        private ConnectionAliasConnectionAliasAssociationAssociationStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectionAliasConnectionAliasAssociationAssociationStatus NotAssociated { get; } = new ConnectionAliasConnectionAliasAssociationAssociationStatus("NOT_ASSOCIATED");
        public static ConnectionAliasConnectionAliasAssociationAssociationStatus PendingAssociation { get; } = new ConnectionAliasConnectionAliasAssociationAssociationStatus("PENDING_ASSOCIATION");
        public static ConnectionAliasConnectionAliasAssociationAssociationStatus AssociatedWithOwnerAccount { get; } = new ConnectionAliasConnectionAliasAssociationAssociationStatus("ASSOCIATED_WITH_OWNER_ACCOUNT");
        public static ConnectionAliasConnectionAliasAssociationAssociationStatus AssociatedWithSharedAccount { get; } = new ConnectionAliasConnectionAliasAssociationAssociationStatus("ASSOCIATED_WITH_SHARED_ACCOUNT");
        public static ConnectionAliasConnectionAliasAssociationAssociationStatus PendingDisassociation { get; } = new ConnectionAliasConnectionAliasAssociationAssociationStatus("PENDING_DISASSOCIATION");

        public static bool operator ==(ConnectionAliasConnectionAliasAssociationAssociationStatus left, ConnectionAliasConnectionAliasAssociationAssociationStatus right) => left.Equals(right);
        public static bool operator !=(ConnectionAliasConnectionAliasAssociationAssociationStatus left, ConnectionAliasConnectionAliasAssociationAssociationStatus right) => !left.Equals(right);

        public static explicit operator string(ConnectionAliasConnectionAliasAssociationAssociationStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectionAliasConnectionAliasAssociationAssociationStatus other && Equals(other);
        public bool Equals(ConnectionAliasConnectionAliasAssociationAssociationStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConnectionAliasConnectionAliasState : IEquatable<ConnectionAliasConnectionAliasState>
    {
        private readonly string _value;

        private ConnectionAliasConnectionAliasState(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectionAliasConnectionAliasState Creating { get; } = new ConnectionAliasConnectionAliasState("CREATING");
        public static ConnectionAliasConnectionAliasState Created { get; } = new ConnectionAliasConnectionAliasState("CREATED");
        public static ConnectionAliasConnectionAliasState Deleting { get; } = new ConnectionAliasConnectionAliasState("DELETING");

        public static bool operator ==(ConnectionAliasConnectionAliasState left, ConnectionAliasConnectionAliasState right) => left.Equals(right);
        public static bool operator !=(ConnectionAliasConnectionAliasState left, ConnectionAliasConnectionAliasState right) => !left.Equals(right);

        public static explicit operator string(ConnectionAliasConnectionAliasState value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectionAliasConnectionAliasState other && Equals(other);
        public bool Equals(ConnectionAliasConnectionAliasState other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
