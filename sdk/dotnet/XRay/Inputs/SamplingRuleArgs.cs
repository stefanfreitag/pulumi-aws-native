// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.XRay.Inputs
{

    public sealed class SamplingRuleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Matches attributes derived from the request.
        /// </summary>
        [Input("attributes")]
        public Input<object>? Attributes { get; set; }

        /// <summary>
        /// The percentage of matching requests to instrument, after the reservoir is exhausted.
        /// </summary>
        [Input("fixedRate")]
        public Input<double>? FixedRate { get; set; }

        /// <summary>
        /// Matches the HTTP method from a request URL.
        /// </summary>
        [Input("hTTPMethod")]
        public Input<string>? HTTPMethod { get; set; }

        /// <summary>
        /// Matches the hostname from a request URL.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        /// <summary>
        /// The priority of the sampling rule.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
        /// </summary>
        [Input("reservoirSize")]
        public Input<int>? ReservoirSize { get; set; }

        /// <summary>
        /// Matches the ARN of the AWS resource on which the service runs.
        /// </summary>
        [Input("resourceARN")]
        public Input<string>? ResourceARN { get; set; }

        [Input("ruleARN")]
        public Input<string>? RuleARN { get; set; }

        [Input("ruleName")]
        public Input<string>? RuleName { get; set; }

        /// <summary>
        /// Matches the name that the service uses to identify itself in segments.
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// Matches the origin that the service uses to identify its type in segments.
        /// </summary>
        [Input("serviceType")]
        public Input<string>? ServiceType { get; set; }

        /// <summary>
        /// Matches the path from a request URL.
        /// </summary>
        [Input("uRLPath")]
        public Input<string>? URLPath { get; set; }

        /// <summary>
        /// The version of the sampling rule format (1)
        /// </summary>
        [Input("version")]
        public Input<int>? Version { get; set; }

        public SamplingRuleArgs()
        {
        }
        public static new SamplingRuleArgs Empty => new SamplingRuleArgs();
    }
}
