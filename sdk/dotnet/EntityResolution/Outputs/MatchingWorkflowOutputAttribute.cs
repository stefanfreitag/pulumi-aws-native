// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EntityResolution.Outputs
{

    [OutputType]
    public sealed class MatchingWorkflowOutputAttribute
    {
        public readonly bool? Hashed;
        public readonly string Name;

        [OutputConstructor]
        private MatchingWorkflowOutputAttribute(
            bool? hashed,

            string name)
        {
            Hashed = hashed;
            Name = name;
        }
    }
}
