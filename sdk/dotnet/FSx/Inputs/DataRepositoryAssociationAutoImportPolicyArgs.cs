// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Inputs
{

    /// <summary>
    /// Specifies the type of updated objects (new, changed, deleted) that will be automatically imported from the linked S3 bucket to your file system.
    /// </summary>
    public sealed class DataRepositoryAssociationAutoImportPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<Pulumi.AwsNative.FSx.DataRepositoryAssociationEventType>? _events;
        public InputList<Pulumi.AwsNative.FSx.DataRepositoryAssociationEventType> Events
        {
            get => _events ?? (_events = new InputList<Pulumi.AwsNative.FSx.DataRepositoryAssociationEventType>());
            set => _events = value;
        }

        public DataRepositoryAssociationAutoImportPolicyArgs()
        {
        }
        public static new DataRepositoryAssociationAutoImportPolicyArgs Empty => new DataRepositoryAssociationAutoImportPolicyArgs();
    }
}
