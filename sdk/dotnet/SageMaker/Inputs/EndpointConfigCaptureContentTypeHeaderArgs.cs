// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class EndpointConfigCaptureContentTypeHeaderArgs : global::Pulumi.ResourceArgs
    {
        [Input("csvContentTypes")]
        private InputList<string>? _csvContentTypes;
        public InputList<string> CsvContentTypes
        {
            get => _csvContentTypes ?? (_csvContentTypes = new InputList<string>());
            set => _csvContentTypes = value;
        }

        [Input("jsonContentTypes")]
        private InputList<string>? _jsonContentTypes;
        public InputList<string> JsonContentTypes
        {
            get => _jsonContentTypes ?? (_jsonContentTypes = new InputList<string>());
            set => _jsonContentTypes = value;
        }

        public EndpointConfigCaptureContentTypeHeaderArgs()
        {
        }
        public static new EndpointConfigCaptureContentTypeHeaderArgs Empty => new EndpointConfigCaptureContentTypeHeaderArgs();
    }
}
