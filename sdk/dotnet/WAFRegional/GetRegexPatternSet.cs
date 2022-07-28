// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFRegional
{
    public static class GetRegexPatternSet
    {
        /// <summary>
        /// Resource Type definition for AWS::WAFRegional::RegexPatternSet
        /// </summary>
        public static Task<GetRegexPatternSetResult> InvokeAsync(GetRegexPatternSetArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegexPatternSetResult>("aws-native:wafregional:getRegexPatternSet", args ?? new GetRegexPatternSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::WAFRegional::RegexPatternSet
        /// </summary>
        public static Output<GetRegexPatternSetResult> Invoke(GetRegexPatternSetInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRegexPatternSetResult>("aws-native:wafregional:getRegexPatternSet", args ?? new GetRegexPatternSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRegexPatternSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetRegexPatternSetArgs()
        {
        }
        public static new GetRegexPatternSetArgs Empty => new GetRegexPatternSetArgs();
    }

    public sealed class GetRegexPatternSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetRegexPatternSetInvokeArgs()
        {
        }
        public static new GetRegexPatternSetInvokeArgs Empty => new GetRegexPatternSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetRegexPatternSetResult
    {
        public readonly string? Id;
        public readonly ImmutableArray<string> RegexPatternStrings;

        [OutputConstructor]
        private GetRegexPatternSetResult(
            string? id,

            ImmutableArray<string> regexPatternStrings)
        {
            Id = id;
            RegexPatternStrings = regexPatternStrings;
        }
    }
}
