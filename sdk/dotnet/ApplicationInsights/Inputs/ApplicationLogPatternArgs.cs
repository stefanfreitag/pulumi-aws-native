// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationInsights.Inputs
{

    /// <summary>
    /// The log pattern.
    /// </summary>
    public sealed class ApplicationLogPatternArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The log pattern.
        /// </summary>
        [Input("pattern", required: true)]
        public Input<string> Pattern { get; set; } = null!;

        /// <summary>
        /// The name of the log pattern.
        /// </summary>
        [Input("patternName", required: true)]
        public Input<string> PatternName { get; set; } = null!;

        /// <summary>
        /// Rank of the log pattern.
        /// </summary>
        [Input("rank", required: true)]
        public Input<int> Rank { get; set; } = null!;

        public ApplicationLogPatternArgs()
        {
        }
    }
}
