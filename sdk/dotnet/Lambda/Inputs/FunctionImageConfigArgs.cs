// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda.Inputs
{

    public sealed class FunctionImageConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("command")]
        private InputList<string>? _command;

        /// <summary>
        /// Command.
        /// </summary>
        public InputList<string> Command
        {
            get => _command ?? (_command = new InputList<string>());
            set => _command = value;
        }

        [Input("entryPoint")]
        private InputList<string>? _entryPoint;

        /// <summary>
        /// EntryPoint.
        /// </summary>
        public InputList<string> EntryPoint
        {
            get => _entryPoint ?? (_entryPoint = new InputList<string>());
            set => _entryPoint = value;
        }

        /// <summary>
        /// WorkingDirectory.
        /// </summary>
        [Input("workingDirectory")]
        public Input<string>? WorkingDirectory { get; set; }

        public FunctionImageConfigArgs()
        {
        }
        public static new FunctionImageConfigArgs Empty => new FunctionImageConfigArgs();
    }
}
