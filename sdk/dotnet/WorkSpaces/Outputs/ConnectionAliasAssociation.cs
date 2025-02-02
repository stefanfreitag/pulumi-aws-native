// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpaces.Outputs
{

    [OutputType]
    public sealed class ConnectionAliasAssociation
    {
        public readonly string? AssociatedAccountId;
        public readonly Pulumi.AwsNative.WorkSpaces.ConnectionAliasAssociationAssociationStatus? AssociationStatus;
        public readonly string? ConnectionIdentifier;
        public readonly string? ResourceId;

        [OutputConstructor]
        private ConnectionAliasAssociation(
            string? associatedAccountId,

            Pulumi.AwsNative.WorkSpaces.ConnectionAliasAssociationAssociationStatus? associationStatus,

            string? connectionIdentifier,

            string? resourceId)
        {
            AssociatedAccountId = associatedAccountId;
            AssociationStatus = associationStatus;
            ConnectionIdentifier = connectionIdentifier;
            ResourceId = resourceId;
        }
    }
}
