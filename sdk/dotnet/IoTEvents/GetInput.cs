// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents
{
    public static class GetInput
    {
        /// <summary>
        /// The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
        /// </summary>
        public static Task<GetInputResult> InvokeAsync(GetInputArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInputResult>("aws-native:iotevents:getInput", args ?? new GetInputArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
        /// </summary>
        public static Output<GetInputResult> Invoke(GetInputInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetInputResult>("aws-native:iotevents:getInput", args ?? new GetInputInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInputArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the input.
        /// </summary>
        [Input("inputName", required: true)]
        public string InputName { get; set; } = null!;

        public GetInputArgs()
        {
        }
        public static new GetInputArgs Empty => new GetInputArgs();
    }

    public sealed class GetInputInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the input.
        /// </summary>
        [Input("inputName", required: true)]
        public Input<string> InputName { get; set; } = null!;

        public GetInputInvokeArgs()
        {
        }
        public static new GetInputInvokeArgs Empty => new GetInputInvokeArgs();
    }


    [OutputType]
    public sealed class GetInputResult
    {
        public readonly Outputs.InputDefinition? InputDefinition;
        /// <summary>
        /// A brief description of the input.
        /// </summary>
        public readonly string? InputDescription;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// 
        /// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        /// </summary>
        public readonly ImmutableArray<Outputs.InputTag> Tags;

        [OutputConstructor]
        private GetInputResult(
            Outputs.InputDefinition? inputDefinition,

            string? inputDescription,

            ImmutableArray<Outputs.InputTag> tags)
        {
            InputDefinition = inputDefinition;
            InputDescription = inputDescription;
            Tags = tags;
        }
    }
}
