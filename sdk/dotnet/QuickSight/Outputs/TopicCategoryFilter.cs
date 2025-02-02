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
    public sealed class TopicCategoryFilter
    {
        public readonly Pulumi.AwsNative.QuickSight.TopicCategoryFilterFunction? CategoryFilterFunction;
        public readonly Pulumi.AwsNative.QuickSight.TopicCategoryFilterType? CategoryFilterType;
        public readonly Outputs.TopicCategoryFilterConstant? Constant;
        public readonly bool? Inverse;

        [OutputConstructor]
        private TopicCategoryFilter(
            Pulumi.AwsNative.QuickSight.TopicCategoryFilterFunction? categoryFilterFunction,

            Pulumi.AwsNative.QuickSight.TopicCategoryFilterType? categoryFilterType,

            Outputs.TopicCategoryFilterConstant? constant,

            bool? inverse)
        {
            CategoryFilterFunction = categoryFilterFunction;
            CategoryFilterType = categoryFilterType;
            Constant = constant;
            Inverse = inverse;
        }
    }
}
