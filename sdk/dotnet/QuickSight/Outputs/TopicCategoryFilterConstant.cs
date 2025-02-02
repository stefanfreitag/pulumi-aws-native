// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TopicCategoryFilterConstant
    {
        public readonly Outputs.TopicCollectiveConstant? CollectiveConstant;
        public readonly Pulumi.AwsNative.QuickSight.TopicConstantType? ConstantType;
        public readonly string? SingularConstant;

        [OutputConstructor]
        private TopicCategoryFilterConstant(
            Outputs.TopicCollectiveConstant? collectiveConstant,

            Pulumi.AwsNative.QuickSight.TopicConstantType? constantType,

            string? singularConstant)
        {
            CollectiveConstant = collectiveConstant;
            ConstantType = constantType;
            SingularConstant = singularConstant;
        }
    }
}
