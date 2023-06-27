// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Events.Inputs
{

    public sealed class ConnectionHttpParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("bodyParameters")]
        private InputList<Inputs.ConnectionParameterArgs>? _bodyParameters;
        public InputList<Inputs.ConnectionParameterArgs> BodyParameters
        {
            get => _bodyParameters ?? (_bodyParameters = new InputList<Inputs.ConnectionParameterArgs>());
            set => _bodyParameters = value;
        }

        [Input("headerParameters")]
        private InputList<Inputs.ConnectionParameterArgs>? _headerParameters;
        public InputList<Inputs.ConnectionParameterArgs> HeaderParameters
        {
            get => _headerParameters ?? (_headerParameters = new InputList<Inputs.ConnectionParameterArgs>());
            set => _headerParameters = value;
        }

        [Input("queryStringParameters")]
        private InputList<Inputs.ConnectionParameterArgs>? _queryStringParameters;
        public InputList<Inputs.ConnectionParameterArgs> QueryStringParameters
        {
            get => _queryStringParameters ?? (_queryStringParameters = new InputList<Inputs.ConnectionParameterArgs>());
            set => _queryStringParameters = value;
        }

        public ConnectionHttpParametersArgs()
        {
        }
        public static new ConnectionHttpParametersArgs Empty => new ConnectionHttpParametersArgs();
    }
}
