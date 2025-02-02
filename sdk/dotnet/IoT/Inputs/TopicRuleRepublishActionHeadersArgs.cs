// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    public sealed class TopicRuleRepublishActionHeadersArgs : global::Pulumi.ResourceArgs
    {
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        [Input("correlationData")]
        public Input<string>? CorrelationData { get; set; }

        [Input("messageExpiry")]
        public Input<string>? MessageExpiry { get; set; }

        [Input("payloadFormatIndicator")]
        public Input<string>? PayloadFormatIndicator { get; set; }

        [Input("responseTopic")]
        public Input<string>? ResponseTopic { get; set; }

        [Input("userProperties")]
        private InputList<Inputs.TopicRuleUserPropertyArgs>? _userProperties;
        public InputList<Inputs.TopicRuleUserPropertyArgs> UserProperties
        {
            get => _userProperties ?? (_userProperties = new InputList<Inputs.TopicRuleUserPropertyArgs>());
            set => _userProperties = value;
        }

        public TopicRuleRepublishActionHeadersArgs()
        {
        }
        public static new TopicRuleRepublishActionHeadersArgs Empty => new TopicRuleRepublishActionHeadersArgs();
    }
}
