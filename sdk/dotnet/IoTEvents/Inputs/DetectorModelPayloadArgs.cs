// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Inputs
{

    /// <summary>
    /// Information needed to configure the payload.
    /// 
    /// By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use `contentExpression`.
    /// </summary>
    public sealed class DetectorModelPayloadArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content of the payload. You can use a string expression that includes quoted strings (`'&lt;string&gt;'`), variables (`$variable.&lt;variable-name&gt;`), input values (`$input.&lt;input-name&gt;.&lt;path-to-datum&gt;`), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.
        /// </summary>
        [Input("contentExpression", required: true)]
        public Input<string> ContentExpression { get; set; } = null!;

        /// <summary>
        /// The value of the payload type can be either `STRING` or `JSON`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DetectorModelPayloadArgs()
        {
        }
        public static new DetectorModelPayloadArgs Empty => new DetectorModelPayloadArgs();
    }
}
