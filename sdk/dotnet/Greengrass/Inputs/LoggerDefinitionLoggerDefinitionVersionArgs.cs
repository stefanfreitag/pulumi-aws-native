// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class LoggerDefinitionLoggerDefinitionVersionArgs : Pulumi.ResourceArgs
    {
        [Input("loggers", required: true)]
        private InputList<Inputs.LoggerDefinitionLoggerArgs>? _loggers;
        public InputList<Inputs.LoggerDefinitionLoggerArgs> Loggers
        {
            get => _loggers ?? (_loggers = new InputList<Inputs.LoggerDefinitionLoggerArgs>());
            set => _loggers = value;
        }

        public LoggerDefinitionLoggerDefinitionVersionArgs()
        {
        }
    }
}
