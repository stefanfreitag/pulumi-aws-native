// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VerifiedPermissions.Inputs
{

    public sealed class PolicyStoreSchemaDefinitionArgs : global::Pulumi.ResourceArgs
    {
        [Input("cedarJson")]
        public Input<string>? CedarJson { get; set; }

        public PolicyStoreSchemaDefinitionArgs()
        {
        }
        public static new PolicyStoreSchemaDefinitionArgs Empty => new PolicyStoreSchemaDefinitionArgs();
    }
}
